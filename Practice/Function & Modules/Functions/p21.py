"""
filter() + lambda
Use filter() and lambda to find all numbers greater than 50:

numbers = [10, 25, 60, 45, 80, 90, 30]
"""

numbers=[10,25,60,45,80,90,30]

fun=lambda x:True if x>50 else False

check=filter(fun,numbers)

print(f"number greater than 50 :{list(check)}")
