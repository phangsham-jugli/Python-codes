#Exception Handling
#1.try-except block

try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter Second number:"))

    result=num1/num2
    print(round(result,2))
except ZeroDivisionError: #we use this cause denominator 0 we cannot divide
    print("Error! Denominator is 0")
except ValueError:
    print("Input should be integer!")