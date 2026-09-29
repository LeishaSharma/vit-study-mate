# Problem Statement & System Design

## 1. Problem Statement

Students frequently face challenges in understanding how their current academic scores and attendance translate into their overall CGPA[cite: 2]. Additionally, setting a goal for a higher CGPA requires determining the exact mark increases needed across individual subjects[cite: 1]. Manual calculation is prone to errors, especially when factoring in conditional criteria such as attendance bonuses and score capping[cite: 1, 3].

**VIT-STUDY-MATE** solves this by automating:
1. Attendance-based bonus criteria calculations[cite: 3].
2. Computation of current percentage and CGPA[cite: 2].
3. Subject-wise target score distribution to achieve a user-defined target CGPA, including capping at maximum possible marks[cite: 1].
4. Automated unit and integration testing to ensure accurate calculations across edge cases[cite: 1, 2, 3].

---

## 2. Key Rules & Formulae

### Attendance Bonus Rule
- If $\text{Attendance} > 75\%$: $\text{Bonus} = 5$ marks[cite: 3].
- $\text{Final Mark} = \min(\text{Raw Mark} + \text{Bonus}, 50)$[cite: 3].

### CGPA Calculations
- $\text{Subject Percentage} = \left( \frac{\text{Final Mark}}{50} \right) \times 100$[cite: 3]
- $\text{Average Percentage} = \frac{\sum \text{Subject Percentage}}{4}$[cite: 2]
- $\text{Current CGPA} = \frac{\text{Average Percentage}}{10}$[cite: 2]

### Target CGPA Redistribution Algorithm
1. $\text{Required Percentage} = \text{Target CGPA} \times 10$[cite: 1]
2. $\text{Increment Percentage} = \text{Required Percentage} - \text{Current Average Percentage}$[cite: 1]
3. $\text{Increment Marks} = \left( \frac{\text{Increment Percentage}}{100} \right) \times 50$[cite: 1]
4. $\text{Initial Target Mark per Subject} = \text{Final Mark} + \text{Increment Marks}$[cite: 1]
5. **Capping & Redistribution**:
   - If any subject's target mark exceeds $50$, the excess points ($\text{Target Mark} - 50$) are collected[cite: 1].
   - Collected excess marks are evenly distributed across remaining subjects that are below $50$ marks, capped at $50$[cite: 1].

---

## 3. Core Modules

| Module File | Primary Responsibility | Key Functions |
| :--- | :--- | :--- |
| `main.py` | Handles interactive execution and user input for 4 subjects | `get_inputs()`, `main()` |
| `display_performance.py` | Evaluates performance metrics and displays academic summary | `performance(subjects)` |
| `calculate_target_cgpa.py` | Calculates required marks for target CGPA and redistributes overflow points | `calculate_target_cgpa(subjects, current_avg_percentage)` |
| `test_main.py` | Executes unit and integration test cases using `unittest` and `unittest.mock` | `TestVITStudyMate` |

---

## 4. Test Suite Design (`test_main.py`)

The system relies on Python's built-in `unittest` framework to validate all core functionality and guard against edge cases without requiring manual user input.

### Key Scenarios Covered:
* **Bonus Capping Logic (`test_get_inputs_with_and_without_attendance_bonus`)**: Verifies that the +5 mark attendance bonus is applied only when attendance exceeds 75% and ensures the final score never exceeds 50[cite: 3].
* **Academic Summary Calculation (`test_performance_calculation`)**: Validates the accurate aggregation of subject percentages into average percentage and final CGPA[cite: 2].
* **Achieved/Higher CGPA State (`test_calculate_target_cgpa_achieved_or_higher`)**: Ensures correct handling when a user inputs a target CGPA less than or equal to their current CGPA[cite: 1].
* **Low Initial Marks Scenario (`test_calculate_target_cgpa_low_marks_improvement`)**: Tests substantial required score increases starting from low baseline performance across all subjects[cite: 1, 2].
* **Target Mark Redistribution (`test_calculate_target_cgpa_redistribution`)**: Validates that excess target points calculated above 50 are properly redistributed across remaining non-capped subjects[cite: 1].
* **Workflow Integration (`test_full_main_workflow`)**: Mocks input streams (`builtins.input`) and standard output (`sys.stdout`) to run the complete CLI execution end-to-end[cite: 1, 2, 3].