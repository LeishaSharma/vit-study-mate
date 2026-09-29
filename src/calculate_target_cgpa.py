MAX_MARKS = 50
ATTENDANCE_BONUS = 5

def calculate_target_cgpa(subjects, current_avg_percentage):
    #Prompts for target CGPA and calculates/displays required mark adjustments in tabular form
    target_cgpa = float(input("\nEnter your targeted CGPA: "))
    required_percentage = target_cgpa * 10
    increment_percentage = required_percentage - current_avg_percentage

    if increment_percentage <= 0:
        if increment_percentage == 0:
            print("\n[INFO] You have already achieved your target CGPA!")
        else:
            print("\n[INFO] Your current CGPA is higher than your target CGPA.")
        return

    increment_marks = (increment_percentage / 100) * MAX_MARKS

    #Calculate target marks per subject
    target_marks = [sub["final_mark"] + increment_marks for sub in subjects]

    adjusting_marks_total = 0
    count = 0

    #Cap at MAX_MARKS and aggregate excess marks
    for i in range(len(target_marks)):
        if target_marks[i] >= MAX_MARKS:
            adjusting_marks_total += target_marks[i] - MAX_MARKS
            count += 1
            target_marks[i] = MAX_MARKS

    #Redistribute excess marks to remaining subjects under MAX_MARKS
    remaining_subjects = len(subjects) - count
    if count > 0 and remaining_subjects > 0:
        average_adjusting_marks = adjusting_marks_total / remaining_subjects
        for i in range(len(target_marks)):
            if target_marks[i] < MAX_MARKS:
                target_marks[i] = min(target_marks[i] + average_adjusting_marks, MAX_MARKS)

    #Output Table: Target Performance Analysis
    print("\n" + "=" * 60)
    print(f"{'TARGET CGPA ANALYSIS & REQUIRED MARKS':^60}")
    print("=" * 60)
    print(f"{'Target CGPA:':<35} {target_cgpa:>6.2f}")
    print(f"{'Required Overall Percentage:':<35} {required_percentage:>6.2f}%")
    print(f"{'Required Percentage Increment:':<35} +{increment_percentage:>5.2f}%")
    print("-" * 60)
    print(f"{'Subject Name':<25} | {'Required Increase':<17} | {'Target Marks':<12}")
    print("-" * 60)

    for i, sub in enumerate(subjects):
        required_increase = target_marks[i] - sub["final_mark"]
        print(f"{sub['name']:<25} | +{required_increase:>6.2f} marks     | {target_marks[i]:>5.2f} / {MAX_MARKS}")

    print("=" * 60)