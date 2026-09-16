"""
Function as argument + lambda
Create a function:

def operate(func, a, b):

Pass different lambda functions to it for:

addition
subtraction
multiplication
division
"""

def operate(func,a,b):

    return func(a,b)

add=lambda a,b:a+b
sub=lambda a,b:a-b
multi=lambda a,b:a*b
div=lambda a,b:a//b

print(operate(add,2,3))
print(operate(sub,5,3))
print(operate(multi,2,3))
print(operate(div,18,2))