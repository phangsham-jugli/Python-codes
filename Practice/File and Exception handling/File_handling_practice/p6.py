"""
6. Append information
Create a program that asks the user for a new student's information and appends it to the existing students.txt without deleting the previous data.
"""
age=int(input("Enter your age:"))
course=input("Enter your course:")
with open('Student.txt','ta') as fh:
    data=fh.write(f"Age:{age}\n"
                  f"Course:{course}")