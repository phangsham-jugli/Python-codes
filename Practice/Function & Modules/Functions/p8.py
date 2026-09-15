"""
Create a function:
The age should have a default value of 18.
"""

def info(name,age=18):
    print(f"Name:{name}|age:{age}")

n=input("Enter your Name:")

info(n)