# 🧠 File Automation Tool (with Database Logging)

A Python command-line project that automates file organization, renaming, and backup tasks — and logs all activities in a SQLite database for easy tracking.

---

## 🚀 Features

✅ Organize files into folders based on file type

✅ Rename multiple files with a custom prefix

✅ Create backups of entire folders

✅ Log every action (organize, rename, backup) in a **SQLite database** 

✅ View logs directly from the command line

---

## 🛠️ Technologies Used

* **Python 3**
* **SQLite (for database logging)**
* Built-in modules: `os`, `shutil`, `sqlite3`, `datetime`

---

## ⚙️ How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/<your-username>/File-Automation-Tool.git
   ```
2. Navigate into the project folder:

   ```bash
   cd File-Automation-Tool
   ```
3. Run the script:

   ```bash
   python automation_tool_db.py
   ```

---

## 🧭 Menu Options

| Option | Description              |
| ------ | ------------------------ |
| 1      | Organize Files by Type   |
| 2      | Rename Files with Prefix |
| 3      | Backup a Folder          |
| 4      | View Logs from Database  |
| 5      | Exit                     |

---

## 📂 Example Log Entry (in Database)

| id | action_type | file_name | source_path | destination_path | timestamp           |
| -- | ----------- | --------- | ----------- | ---------------- | ------------------- |
| 1  | organize    | notes.txt | /Downloads  | /Documents/Text  | 2025-10-18 14:23:11 |

---

## 💡 Future Improvements

* Add scheduling to automate tasks daily
* Add GUI using Tkinter
* Cloud backup integration (Google Drive or AWS S3)

---

## 👩‍💻 Author

**Pavani**
Final Year B.Tech Student | Python Developer
📧 [[your.email@example.com](mailto:your.email@example.com)]
🌐 [Your GitHub Profile Link]
