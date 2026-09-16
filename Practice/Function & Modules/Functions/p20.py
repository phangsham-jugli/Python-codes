"""
filter() + lambda
Given:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Use filter() and lambda to find all even numbers.
"""
numbers=[1,2,3,4,5,7,8,9,10]

fun=lambda x:True if x%2==0 else False

checkEven=filter(fun,numbers)
print(f"Even number are:{list(checkEven)}")

