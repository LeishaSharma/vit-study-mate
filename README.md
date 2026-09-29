# VIT-StudyMate

**VIT-StudyMate** is a Python CLI utility designed to help students track their current academic performance and plan ahead by calculating required mark increases per subject to reach a targeted CGPA.

---

## Features

- **Attendance Bonus Logic**: Automatically applies a +5 mark bonus for subjects with attendance above 75%, capped at a maximum of 50 marks.
- **Academic Performance Summary**: Displays subject details, attendance, adjusted final marks, percentages, average percentage, and current CGPA.
- **Target CGPA Analysis**:
  - Calculates the overall percentage increase needed to reach a target CGPA.
  - Generates required mark increases per subject.
  - Automatically redistributes excess target marks when individual subject scores reach the maximum limit (50/50).
- **Unit Testing**: Fully tested CLI interaction and mark distribution logic using Python's `unittest` and `unittest.mock`.

---

## File Structure

```text
├── calculate_target_cgpa.py   # Handles target CGPA calculations & mark redistribution
├── display_performance.py    # Formats and displays current performance summary
├── main.py                    # Application entry point and user input flow
└── test_main.py               # Automated unit and integration tests