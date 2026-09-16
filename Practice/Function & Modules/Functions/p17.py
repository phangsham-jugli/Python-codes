"""
map() + lambda
Given:

numbers = [1, 2, 3, 4, 5]

Use map() and lambda to create a list containing the squares.
"""

numbers=[1,2,3,4,5]
fun=lambda x:x**2
sqr=map(fun,numbers)
newsqr=list(sqr)
print(newsqr)