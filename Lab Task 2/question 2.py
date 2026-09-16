name = input("Enter Student Name: ")
print("Enter marks out of 100:")
math = float(input("Enter Mathematics marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
english = float(input("Enter English marks: "))
computer = float(input("Enter Computer Science marks: "))

total = math + physics + chemistry + english + computer
percentage = (total / 500) * 100


if math < 40:
    result = "FAIL"
    grade = "F"
elif physics < 40:
    result = "FAIL"
    grade = "F"
elif chemistry < 40:
    result = "FAIL"
    grade = "F"
elif english < 40:
    result = "FAIL"
    grade = "F"
elif computer < 40:
    result = "FAIL"
    grade = "F"
elif percentage >= 80:
    result = "PASS"
    grade = "A+"
elif percentage >= 70:
    result = "PASS"
    grade = "A"
elif percentage >= 60:
    result = "PASS"
    grade = "B"
elif percentage >= 50:
    result = "PASS"
    grade = "C"
elif percentage >= 40:
    result = "PASS"
    grade = "D"
else:
    result = "FAIL"
    grade = "F"


print("STUDENT MARKSHE")
print("Name        :", name)
print("Mathematics :", math)
print("Physics     :", physics)
print("Chemistry   ", chemistry)
print("English     :", english)
print("Computer    :", computer)
print("Total Marks :", total, "/ 500")
print("Percentage  :", percentage, "%")
print("Grade       :", grade)
print("Result      ", result)