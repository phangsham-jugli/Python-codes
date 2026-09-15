"""
7. Write a function student_info(name, age, course) that prints the student's information.
Call it using:
positional arguments
keyword arguments
"""

def Student_info(name,age,course):
    print(f"Name of student is :{name}")
    print(f"Age:{age}")
    print(f"Course:{course}")
    print("\n")

n=input("Enter your name:")
a=int(input("Enter your age:"))
c=input("Enter your course:")

#Positional arguments
Student_info(n,a,c)

#Keyword argument
Student_info(name="Mark",age=12,course="Bca")