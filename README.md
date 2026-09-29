# VIT Bhopal Academic Helper (26BCE)

A lightweight, terminal-based Python utility designed specifically for B.Tech CSE students to track academic progress, calculate relative grades, and manage FFCS attendance requirements. Built entirely with core Python, this project is designed to be fast, reliable, and completely dependency-free.

## Features

1. **Relative Grading Calculator:** Calculates your expected grade for CAT exams (out of 50) using a dynamic relative grading curve based on the class average.
2. **FFCS Attendance Tracker:** Calculates your current attendance percentage and uses algebraic logic to tell you exactly how many upcoming classes you can safely skip (or must attend) to maintain the mandatory 75% threshold.
3. **SGPA Estimator:** Estimates your Semester Grade Point Average on a 10-point scale based on the credits and expected grades of your current courses.
4. **Study Priority Finder:** Compares the marks of three subjects and flags the weakest one that requires immediate study focus.

## Technical Constraints
* **Language:** Python 3.x
* **Dependencies:** None. This program deliberately avoids external modules (like `math`) or libraries to demonstrate a strong grasp of foundational programming concepts, custom logic, and control flow.

## How to Run

Since this project requires no external installations, you can run it directly from your terminal. 

1. Open your terminal (or VS Code terminal in WSL/Ubuntu).
2. Navigate to the directory containing the file.
3. Execute the script:
   ```bash
   python3 academic_helper.py