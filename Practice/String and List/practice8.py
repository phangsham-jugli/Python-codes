# Perform:
# Add a new student
# Remove "Amit"
# Sort the list
# Check whether "Priya" exists
# Print the first and last student

students = ["Rahul", "Amit", "Priya", "Ankit", "Neha"]
new=students.extend(["kumar","lalit"])
print(students)
r=students.remove("Amit")
print(students)

print("Priya" in students)

print(students[0])
print(students[-1])