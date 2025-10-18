import os
import shutil
import sqlite3
from datetime import datetime

# --------------------- DATABASE SETUP ---------------------

def init_db():
    """Create a SQLite database and tasks table if not exists."""
    conn = sqlite3.connect('automation_log.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    action_type TEXT,
                    file_name TEXT,
                    source_path TEXT,
                    destination_path TEXT,
                    timestamp TEXT
                )''')
    conn.commit()
    conn.close()

def log_to_db(action_type, file_name, source, destination):
    """Insert a record of performed action into the database."""
    conn = sqlite3.connect('automation_log.db')
    c = conn.cursor()
    c.execute('''INSERT INTO tasks (action_type, file_name, source_path, destination_path, timestamp)
                 VALUES (?, ?, ?, ?, ?)''',
              (action_type, file_name, source, destination, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

# --------------------- CORE FUNCTIONS ---------------------

def organize_files(folder_path):
    """Organize files into subfolders by extension."""
    try:
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                ext = file.split('.')[-1].upper()
                dest_folder = os.path.join(folder_path, ext)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, dest_folder)
                log_to_db('Organize', file, folder_path, dest_folder)
        print("✅ Files organized successfully!")
    except Exception as e:
        print("❌ Error organizing files:", e)

def rename_files(folder_path, prefix):
    """Rename all files in the folder with a given prefix."""
    try:
        count = 1
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                ext = file.split('.')[-1]
                new_name = f"{prefix}_{count}.{ext}"
                new_path = os.path.join(folder_path, new_name)
                os.rename(file_path, new_path)
                log_to_db('Rename', new_name, file_path, new_path)
                count += 1
        print("✅ Files renamed successfully!")
    except Exception as e:
        print("❌ Error renaming files:", e)

def backup_folder(source_folder, backup_folder):
    """Copy all files from source to backup folder."""
    try:
        os.makedirs(backup_folder, exist_ok=True)
        for file in os.listdir(source_folder):
            file_path = os.path.join(source_folder, file)
            if os.path.isfile(file_path):
                shutil.copy(file_path, backup_folder)
                log_to_db('Backup', file, source_folder, backup_folder)
        print("✅ Backup completed successfully!")
    except Exception as e:
        print("❌ Error creating backup:", e)

def view_logs():
    """View all logged actions from the database."""
    try:
        conn = sqlite3.connect('automation_log.db')
        c = conn.cursor()
        c.execute("SELECT * FROM tasks ORDER BY id DESC")
        rows = c.fetchall()
        conn.close()

        if not rows:
            print("📭 No logs found.")
            return

        print("\n📜 Task Log:")
        print("-" * 80)
        for row in rows:
            print(f"ID: {row[0]} | Action: {row[1]} | File: {row[2]} | From: {row[3]} | To: {row[4]} | Time: {row[5]}")
        print("-" * 80)
    except Exception as e:
        print("❌ Error reading logs:", e)

# --------------------- MAIN MENU ---------------------

def main():
    init_db()
    while True:
        print("\n--- Task Automation Tool with Database Logging ---")
        print("1. Organize Files")
        print("2. Rename Files")
        print("3. Backup Folder")
        print("4. View Logs")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            folder = input("Enter folder path to organize: ")
            organize_files(folder)
        elif choice == '2':
            folder = input("Enter folder path to rename files: ")
            prefix = input("Enter prefix for renamed files: ")
            rename_files(folder, prefix)
        elif choice == '3':
            src = input("Enter source folder path: ")
            dest = input("Enter backup folder path: ")
            backup_folder(src, dest)
        elif choice == '4':
            view_logs()
        elif choice == '5':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
