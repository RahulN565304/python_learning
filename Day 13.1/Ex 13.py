student_marks = (80, 90, 75, 90, 95)

def get_average_highest_lowest_grade(student_marks):
    total = sum(student_marks)
    average = total / len(student_marks)
    if average >= 90:
        grade = "Excellent"
    elif average >=80:
        grade = "Good"
    elif average >=60:
        grade = "Average"
    else :
        grade = "Poor"
    highest = max(student_marks)
    lowest = min(student_marks)
    return average, highest, lowest, grade

avg, high, low, grade = get_average_highest_lowest_grade(student_marks)
print(f"the average of student is : {avg}")
print(f"The highest mark is : {high}")
print(f"The lowest mark is : {low}")
print(f"The grade is : {grade}")