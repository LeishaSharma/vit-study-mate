import sys
from display_performance import performance
from calculate_target_cgpa import calculate_target_cgpa

MAX_MARKS = 50
ATTENDANCE_BONUS = 5

def get_inputs():
    #Collects subject details, marks, and attendance from the user
    subjects = []

    for i in range(1, 5):
        name = input(f"\nEnter name of Subject {i}: ")
        raw_mark = float(input(f"Enter marks obtained in {name} (out of 50): "))
        attendance = float(input(f"Enter attendance percentage in {name} (%): "))

        #Apply attendance bonus if attendance > 75%, capped at MAX_MARKS
        bonus = ATTENDANCE_BONUS if attendance > 75 else 0
        final_mark = min(raw_mark + bonus, MAX_MARKS)

        subjects.append({
            "name": name,
            "raw_mark": raw_mark,
            "attendance": attendance,
            "final_mark": final_mark,
            "percentage": (final_mark / MAX_MARKS) * 100
        })

    return subjects

def main():
    print("===============================================================================")
    print("                             VIT-StudyMate                                     ")
    print("===============================================================================")
    candidate_name = input("Your name: ")
    print("WELCOME TO VIT-StudyMate", candidate_name)

    #Input Function
    subjects_data = get_inputs()

    #Display Function
    avg_percentage, _ = performance(subjects_data)

    #Calculate Function
    calculate_target_cgpa(subjects_data, avg_percentage)

if __name__ == "__main__":
    main()