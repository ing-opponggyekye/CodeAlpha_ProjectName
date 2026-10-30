# CodeAlpha - Hangman Game

## Overview
This project is developed as part of the **CodeAlpha Python Programming Internship** (Task 1: Hangman Game). It is a classic text-based Hangman game implemented in Python where players attempt to guess a secret word one letter at a time within a limited number of attempts.

---

## Features
* **ASCII Art Visuals**: Dynamic ASCII gallows and hangman stages that update progressively with each incorrect guess.
* **Randomized Secret Word**: Selects a word at random from a predefined bank of programming and tech terms.
* **Visual Word Tracking**: Displays correctly guessed letters in place while hiding remaining letters as underscores (`_`).
* **Input Validation**: Rejects invalid inputs (numbers, special characters, multi-letter strings) and warns against duplicate guesses without penalty.
* **Replay Option**: Prompt to play multiple rounds upon game win or loss.

---

## Prerequisites & Requirements
* **Python 3.x**
* Standard Python modules used: `random`, `sys` (No external packages required).

---

## How to Play

1. **Clone the Repository**:
   ```bash
   git clone <your-github-repo-url>
   cd CodeAlpha_HangmanGame
   ```

2. **Launch the Game**:
   ```bash
   python hangman_game.py
   ```

3. **Game Rules**:
   * Guess one letter per turn.
   * You are allowed up to **6 incorrect guesses**.
   * Guessing all letters in the word results in a victory!

---

## Repository Structure
```text
Task_1_HangmanGame/
├── hangman_game.py      # Main game script
└── README.md            # Project documentation
```

---

