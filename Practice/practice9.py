# Using list indexing, print:
# Rahul's marks
# Priya's name
# Neha's marks
# The complete second student's information

# Then change Amit's marks from 72 to 80.

students = [
    ["Rahul", 85],
    ["Amit", 72],
    ["Priya", 91],
    ["Neha", 68]
]

print(f"the marks of Rahul is {students[0][1]}")
print(students[3][0])
print(f"the marks of neha is {students[3][-1]}")

students[1][1]=80
print(students)