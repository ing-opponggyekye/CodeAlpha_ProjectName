# CodeAlpha Python Programming Internship - Completed Tasks

## Overview
This repository contains the complete set of Python projects developed for the **CodeAlpha Python Programming Internship**:A summarization of the implentation and codes for the Three tasks I completed.

This repository includes implementations for **Three(3) Completed Tasks**:
1. **Task 1: Hangman Game**
2. **Task 3: Task Automation (File Organizer)**
3. **Task 4: Basic Chatbot**

---

## Repository Structure

```text
CodeAlpha_Python_Internship/
│
├── Task_1_HangmanGame/
│   ├── hangman_game.py       # Text-based Hangman game with ASCII visuals
│   └── README.md             # Task 1 documentation
│
├── Task_3_TaskAutomation/
│   ├── file_organizer.py     # Automated script to organize .jpg/.jpeg files
│   └── README.md             # Task 3 documentation
│
├── Task_4_BasicChatbot/
│   ├── basic_chatbot.py      # Rule-based terminal chatbot
│   └── README.md             # Task 4 documentation
│
└── README.md                 # Master repository documentation
```

---

## Project Summaries

### Task 1: Hangman Game (`hangman_game.py`)
* **Goal**: A text-based guessing game where a players try to guess a secret word letter by letter within 6 attempts. The interface comprises of a stickman being hang anytime a wrong guess is made.
* **Key Features**: ASCII stage visuals, input validation, duplicate guess detection, randomized secret word selection.
* **Usage**:
  ```bash
  python Task_1_HangmanGame/hangman_game.py
  ```

### Task 3: Task Automation - File Organizer (`file_organizer.py`)
* **Goal**: Automate file management by scanning a directory and transferring image files (`.jpg`/`.jpeg`) to a designated folder.
* **Key Features**: Case-insensitive extension matching, filename collision handling, folder safety checks.
* **Usage**:
  ```bash
  python Task_3_TaskAutomation/file_organizer.py "/path/to/source" "/path/to/destination"
  ```

### Task 4: Basic Chatbot (`basic_chatbot.py`)
* **Goal**: Build an interactive CLI chatbot using rule-based natural language processing.
* **Key Features**: Intent recognition via regular expressions, input normalization, interactive chat loop, graceful exit commands (`bye`, `exit`).
* **Usage**:
  ```bash
  python Task_4_BasicChatbot/basic_chatbot.py
  ```

---
