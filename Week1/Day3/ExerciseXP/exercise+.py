import statistics

student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

student_averages = {}
student_letter_grades = {}
total_grade = 0
def student_report():

    for i in student_grades:
        student_averages[i] = statistics.mean(student_grades[i])
    print(student_averages)

    for i in student_averages:
        if student_averages[i] >= 90:
            student_letter_grades[i] = 'A'
            print(f"{student_averages[i]}: {student_letter_grades[i]}")
        elif student_averages[i] >= 80 and student_averages[i] <= 89:
            student_letter_grades[i] = 'B'
            print(f"{student_averages[i]}: {student_letter_grades[i]}")
        elif student_averages[i] >= 70 and student_averages[i] <= 79:
            student_letter_grades[i] = 'C'
            print(f"{student_averages[i]}: {student_letter_grades[i]}")
        elif student_averages[i] >= 60 and student_averages[i] <= 69:
            student_letter_grades[i] = 'D'
            print(f"{student_averages[i]}: {student_letter_grades[i]}")
        else:
            student_letter_grades[i] = 'F'
            print(f"{student_averages[i]}: {student_letter_grades[i]}")
    avg_grade =  sum(student_averages.values()) / len(student_averages.keys())
    print(avg_grade)
student_report()
