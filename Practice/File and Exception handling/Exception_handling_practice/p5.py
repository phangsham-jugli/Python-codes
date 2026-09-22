"""
Multiple Exceptions
Write a program that takes two numbers and performs division. Handle both:
- ValueError
- ZeroDivisionError
"""
try:
    a=int(input("Enter a numerator:"))
    b=int(input("Enter a denominator:"))
    num=a/b
except ValueError as er:
    print(er)
except ZeroDivisionError as zd:
    print(zd)
else:
    print(num)