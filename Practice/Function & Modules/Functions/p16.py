"""
5. Lambda
Write a lambda function that takes two numbers and returns the larger number.
"""
a=int(input("Enter first number:"))

b=int(input("Enter second number:"))



check = lambda num1, num2: num1 if num1 > num2 else num2

result = check(a, b)

print("Larger number:", result)
