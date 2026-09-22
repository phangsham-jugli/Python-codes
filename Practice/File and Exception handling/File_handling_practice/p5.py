"""
5. Write student information
Take the following information from the user:
- Name
- Roll number
- Marks
Store it in students.txt using write mode.
"""

name=input("Enter your name:")
roll=int(input("Enter your roll no:"))
marks=float(input("Enter your marks:"))

with open("Student.txt",'tw') as fh:
    data=fh.write(f"Name:{name}\n"
                  f"Roll No:{roll}\n"
                  f"marks:{marks}\n")


