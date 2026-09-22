"""
Divide Two Numbers
Write a program that takes two numbers from the user and handles the ZeroDivisionError if the second number is 0.
"""
a=int(input("Enter number for a:"))
b=int(input("Enter number for b:"))
try:
    num=a/b
except ZeroDivisionError as zr:
    print("Error due to denominator is zero")
    print(zr)