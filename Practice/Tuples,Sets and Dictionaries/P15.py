#Create a dictionary:
students = {
    "Rahul": 85,
    "Amit": 72,
    "Priya": 91,
    "Neha": 68
}

# Perform all of these:
# Print all student names.
# Print all marks.
# Print Priya's marks.
# Change Neha's marks to 75.
# Add "Rohit": 88.
# Delete Amit.
# Find the highest marks.
# Find the lowest marks.
# Calculate the total of all marks.
# Calculate the average marks.

print(f'Names of students:{students.keys()}\n')

print(f'All marks are:{students.values()}\n')

print(f"Neha's Marks is:{students['Neha']}\n")

students["Neha"]=75

students["Rohit"]=88

students.pop("Amit")

print(f"Higest marks is:{max(students.values())}\n")

print(f"Lowest marks is:{min(students.values())}\n")

total=sum(students.values())
print(f"Total marks of students:{total}\n")

av=total/len(students)

print(f"average marks:{av}")



