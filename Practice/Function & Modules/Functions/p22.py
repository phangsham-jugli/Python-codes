"""filter() + lambda
Given:

numbers = [12, 15, 18, 21, 24, 27, 30]

Find all numbers that are divisible by 3 and even."""

numbers= [12, 15, 18, 21, 24, 27, 30]

fun=lambda x:True if x%2==0 and x%3==0 else False

check=filter(fun,numbers)

print(list(check))
