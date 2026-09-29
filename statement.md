---

### statement.md

```markdown
# Problem Statement: Freshman Academic Management System

## Background
Navigating university academic systems for the first time can be overwhelming for freshmen. Between tracking relative grading curves for CAT examinations and meticulously managing the 75% minimum attendance criteria under the Fully Flexible Credit System (FFCS), students often rely on guesswork or manual calculations. Miscalculating attendance margins can lead to debarment, while misunderstanding the relative grading curve can lead to poor academic planning.

## Objective
To develop a terminal-based software solution in Python that automates these critical academic calculations. The program aims to remove the guesswork from academic planning by providing precise, personalized data regarding grades, attendance margins, and semester performance.

## Project Scope
The system handles four primary operations:
1. Processing individual student marks against the class average to determine relative grades (S, A, B, C, D, F).
2. Evaluating attendance data to output the exact number of future classes a student can afford to miss, or the consecutive classes they must attend to avoid falling below 75%.
3. Aggregating course credits and projected grades to compute an estimated SGPA.
4. Analyzing performance across multiple subjects to recommend study priorities.

## Methodology & Technical Approach
The project is built entirely on foundational programming principles to demonstrate core competency in Python. 
* **Control Flow:** Utilizes `while` loops for the primary navigation menu and `for` loops for iterative data collection (e.g., calculating SGPA across multiple subjects).
* **Conditional Logic:** Deeply nested `if-elif-else` structures handle the relative grading brackets and the distinct scenarios for attendance margins.
* **Algorithmic Problem Solving:** Custom mathematical logic is used in place of built-in libraries. For example, manual ceiling logic is applied to the attendance recovery calculation without importing the `math` module, and manual variable comparison is used to find minimum values without relying on the `min()` function.

## Target Audience
First-year B.Tech engineering students requiring a fast, local, and reliable tool to manage their semester academics from the command line.