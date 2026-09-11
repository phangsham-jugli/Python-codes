# To write a function of calculator

def calcu(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b


op = input("Choose operator: +, -, /, *: ")

if op not in ['+', '-', '/', '*']:
    print("Invalid operator")
else:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))

    result = calcu(a, b, op)

    if op == '+':
        print(f"Value of {a} + {b} = {result}")
    elif op == '-':
        print(f"Value of {a} - {b} = {result}")
    elif op == '*':
        print(f"Value of {a} * {b} = {result}")
    elif op == '/':
        print(f"Value of {a} / {b} = {result}")