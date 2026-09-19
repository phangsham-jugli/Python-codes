#Raising Error

salary=float(input("Enter the salary:"))

if salary <0:
    raise ValueError("Salary cannot be 0")
else:
    print("Your salary is ",salary)