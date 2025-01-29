marks = int(input("Enter your marks: "))

if marks < 70:
    grade = 'D'
elif marks >= 70 and marks < 80:
    grade = 'C'
elif marks >= 80 and marks < 90:
    grade = 'B'
elif marks >= 90:
    grade = 'A'

print("Your grade is: ", grade)