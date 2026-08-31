#Set Difference

# Find:
# Students learning both Python and Java
# Students learning only Python
# Students learning only Java
# All students

students_python = {"Rahul", "Amit", "Priya", "Neha"}
students_java = {"Amit", "Neha", "Rohit"}

Inter=students_java & students_python
print(f"Student learning java and Python are:{Inter}\n")

SP=students_python-students_java
print(f"Student learning only Python:{SP}\n")

SJ=students_java-students_python
print(f"Student learning only java:{SJ}\n")

As=students_python.union(students_java)
print(f"List of all student:{As}")