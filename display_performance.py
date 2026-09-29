MAX_MARKS = 50
ATTENDANCE_BONUS = 5

def performance(subjects):
    #Calculates current CGPA and displays academic performance
    total_percentage = sum(sub["percentage"] for sub in subjects)
    average_percentage = total_percentage / len(subjects)
    cgpa = average_percentage / 10

    print("\n" + "=" * 68)
    print(f"{'CURRENT ACADEMIC PERFORMANCE':^68}")
    print("=" * 68)
    print(f"{'Subject Name':<20} | {'Att. %':<8} | {'Final Marks':<14} | {'Percentage':<8}")
    print("-" * 68)

    for sub in subjects:
        print(f"{sub['name']:<20} | {sub['attendance']:>6.1f}% | {sub['final_mark']:>5.2f} / {MAX_MARKS}   | {sub['percentage']:>7.2f}%")

    print("-" * 68)
    print(f"{'Average Percentage:':<32} {average_percentage:>6.2f}%")
    print(f"{'Current CGPA:':<32} {cgpa:>6.2f}")
    print("=" * 68)

    return average_percentage, cgpa