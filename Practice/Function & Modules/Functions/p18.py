"""
Given:
numbers = [1, 2, 3, 4, 5]

 map() + lambda
Given a list of numbers, use map() to add 10 to every number.
"""

numbers=[1,2,3,4,5]
fun=lambda x:x+10

new=map(fun,numbers)
newnum=list(new)
print(newnum)