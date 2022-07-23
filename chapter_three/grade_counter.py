grades = int(input("Enter student score or -2 to stop: "))

total = 0
counter = 0
while grades != -2:
    total += grades
    counter += 1
    grades = int(input("Enter student score or -2 to stop: "))

if grades != 0:
    grade_score = total / counter
    print(f"The average grade score is {grade_score:.2f}")

