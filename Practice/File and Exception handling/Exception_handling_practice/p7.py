"""
Raise an Exception
Write a program that asks the user for their age. If the age is less than 18, use raise to generate an exception with the message "Not eligible".
"""
age=int(input("Enter your age:"))
if age<0:
    raise Exception("Age cannot be negative")
elif age<18:
    raise Exception("Not eligible to vote")
else:
    print("You can vote!")

