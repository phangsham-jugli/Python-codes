"""
2. Integer Input
Write a program that asks the user to enter an integer. Handle the ValueError if the user enters something other than a number.
"""
try:
    a=int(input("Enter number:"))
except ValueError as VE:
    print("Error enter correct input")
    print(VE)
