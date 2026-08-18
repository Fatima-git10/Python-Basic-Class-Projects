
# Write a program to show student grading system in Python.

print("Enter your marks obtained in 4 subjects: ")

english = int(input("English: "))

maths = int(input("Maths: "))

science = int(input("Science: "))

social = int(input("Social: "))

total_marks = english + maths + science + social

average = int(total_marks / 4)

if average in range(81,100 ):

    print("Grade A")

elif average in range(61,80 ):

    print("Grade B")

elif average in range(41,60 ):

    print("Grade C")

else:

    print("Grade F")