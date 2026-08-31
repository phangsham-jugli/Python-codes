#Tuple inside Dictionary
#Given
students = {
    "Rahul": (85, 90, 88),
    "Amit": (70, 75, 80),
    "Priya": (95, 92, 98)
}

# Print:
# Rahul's first mark
# Amit's last mark
# Priya's second mark
# Then calculate Rahul's total marks.

print(f'Marks of rahul is:{students["Rahul"]}\n')
print(f"Amit's FIRST marks is {students['Amit'][0]}\n")
print(f"Priya's Second marks:{students['Priya'][1]}\n")

total=sum(students["Rahul"])
print(f'total marks of Rahul is:{total}')