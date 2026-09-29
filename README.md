# VIT-STUDY-MATE

**VIT-STUDY-MATE** is a Python-based CLI application designed to help students track their current academic performance and plan the marks required to achieve a target CGPA.

## Features

- **Attendance-Bonus Logic**: Automatically adds a 5-mark bonus to subjects where attendance exceeds 75% (capped at 50 marks maximum).
- **Academic-Performance Overview**: Calculates and presents subject-wise raw marks, final marks, percentage, average percentage, and current CGPA in a clean tabular view.
- **Target-CGPA Planning**: Calculates the percentage and mark increments needed to achieve a target CGPA.
- **Smart-Mark Redistribution**: Redistributes excess marks to other subjects if a target score exceeds the maximum mark cap (50).

## Project Structure

```text
VIT-StudyMate/
├── main.py                    # Program entry point and user input handler
├── display_performance.py     # Calculates and displays current academic metrics
└── calculate_target_cgpa.py   # Calculates mark adjustments for target CGPA