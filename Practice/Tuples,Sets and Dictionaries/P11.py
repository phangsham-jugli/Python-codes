#Nested Dictionary
#Given:

students = {
    "student1": {"name": "Rahul", "marks": 85},
    "student2": {"name": "Amit", "marks": 72},
    "student3": {"name": "Priya", "marks": 91}
}

# Print:
# Rahul's marks
# Amit's name
# Priya's marks
# Then change Amit's marks to 80.

Rm=students["student1"]["marks"]
print(f"Marks of rahul is:{Rm}\n")

An=students["student2"]["name"]
print("student 2 name is:",An,"\n")

Pm=students["student3"]["marks"]
print(f'Marks of priya is:{Pm}\n')

students["student2"]["marks"]=80

print(f'Updated students details:{students}')