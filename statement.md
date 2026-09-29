# Problem Statement & System Design

## 1. Problem Statement

Students frequently face challenges in understanding how their current academic scores and attendance translate into their overall CGPA. Additionally, setting a goal for a higher CGPA requires determining the exact mark increases needed across individual subjects. Manual calculation is prone to errors, especially when factoring in conditional criteria such as attendance bonuses and score capping.

**VIT-STUDY-MATE** solves this by automating:
1. Attendance-based bonus criteria calculations.
2. Computation of current percentage and CGPA.
3. Subject-wise target score distribution to achieve a user-defined target CGPA, including capping at maximum possible marks.

---

## 2. Key Rules & Formulae

### Attendance Bonus Rule
- If $\text{Attendance} > 75\%$: $\text{Bonus} = 5$ marks.
- $\text{Final Mark} = \min(\text{Raw Mark} + \text{Bonus}, 50)$.

### CGPA Calculations
- $\text{Subject Percentage} = \left( \frac{\text{Final Mark}}{50} \right) \times 100$
- $\text{Average Percentage} = \frac{\sum \text{Subject Percentage}}{4}$
- $\text{Current CGPA} = \frac{\text{Average Percentage}}{10}$

### Target CGPA Redistribution Algorithm
1. $\text{Required Percentage} = \text{Target CGPA} \times 10$
2. $\text{Increment Percentage} = \text{Required Percentage} - \text{Current Average Percentage}$
3. $\text{Increment Marks} = \left( \frac{\text{Increment Percentage}}{100} \right) \times 50$
4. $\text{Initial Target Mark per Subject} = \text{Final Mark} + \text{Increment Marks}$
5. **Capping & Redistribution**:
   - If any subject's target mark exceeds $50$, the excess points ($\text{Target Mark} - 50$) are collected.
   - Collected excess marks are evenly distributed across remaining subjects that are below $50$ marks, capped at $50$.

---

## 3. Core Modules

| Module File | Primary Responsibility | Key Functions |
| :--- | :--- | :--- |
| `main.py` | Handles interactive execution and user input for 4 subjects | `get_inputs()`, `main()` |
| `display_performance.py` | Evaluates performance metrics and displays academic summary | `performance(subjects)` |
| `calculate_target_cgpa.py` | Calculates required marks for target CGPA and redistributes overflow points | `calculate_target_cgpa(subjects, current_avg_percentage)` |