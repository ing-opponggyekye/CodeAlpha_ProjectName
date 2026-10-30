# CodeAlpha - Task Automation: File Organizer

## Overview
This project is developed as part of the **CodeAlpha Python Programming Internship** (Task 3: Task Automation with Python Scripts). It is an automated file management script that scans a designated source directory and transfers all `.jpg` and `.jpeg` image files into an organized destination folder.

---

## Features
* **Automatic Categorization**: Detects and transfers all `.jpg` and `.jpeg` image files from a source directory.
* **Case-Insensitive Extension Handling**: Seamlessly handles uppercase and lowercase extensions (`.jpg`, `.JPG`, `.jpeg`, `.JPEG`).
* **Collision Resolution**: Automatically renames duplicate filenames in the destination folder to prevent accidental overwrites (e.g., `photo_1.jpg`).
* **Subdirectory Protection**: Validates file system items to ensure subdirectories are not incorrectly moved as files.
* **Execution Summary**: Provides a clear console log detailing every file moved and the total count.

---

## Prerequisites & Requirements
* **Python 3.x**
* Standard Python modules used: `os`, `shutil`, `sys` (No external packages required).

---

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone <your-github-repo-url>
   cd CodeAlpha_TaskAutomation
   ```

2. **Run the Script**:
   ```bash
   python file_organizer.py "/path/to/source_folder" "/path/to/destination_folder"
   ```

   *If no folder paths are provided, the script defaults to searching `./source_folder` and moving images to `./jpg_folder`.*

---

## Repository Structure
```text
Task_3_TaskAutomation/
├── file_organizer.py    # Main automation script
└── README.md            # Project documentation
```

---

