#Dictionary Access
# Given:

student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python",
    "marks": 85
}

# Print:
# Student's name
# Age
# Course
# Marks
# Then change the marks to 90.

print(student["name"])
print(student["age"])
print(student["course"])
print(student["marks"])

student["marks"]=90
print(f'New marks of student with details{student}')