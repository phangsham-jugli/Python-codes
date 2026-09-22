"""
4. Dictionary Key
Create a dictionary containing student names and marks. Ask the user for a student name and handle the KeyError if the name doesn't exist.
"""
students = {
    "Prakash": 88,
    "Rahul": 75,
    "Aman": 92
}

try:
    na = input("Enter name: ")
    print("Marks:", students[na])

except KeyError:
    print("Error: Student does not exist")