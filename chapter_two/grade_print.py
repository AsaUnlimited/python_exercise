grade = int(input("Enter Exam Score:"))
if 90 <= grade <= 100:
    print(f'Congratulations! Your grade of {grade} earns you an A+ in this course')
elif 80 <= grade <= 90:
    print(f'Congratulations! Your grade of {grade} earns you an A in this course')
elif 70 <= grade <= 80:
    print(f'Congratulations! Your grade of {grade} earns you an B in this course')
elif 60 <= grade <= 70:
    print(f'Congratulations! Your grade of {grade} earns you an C in this course')
elif 50 <= grade <= 60:
    print(f'Congratulations! Your grade of {grade} earns you an D in this course')
else:
    print(f'Your grade of {grade} earns you an F in this course, You need to retake this course')
