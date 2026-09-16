"""
2. Function as an argument
Create a function apply_function(func, number) that takes a function and a number,
then returns the result of applying the function to the number.
"""

def app(num,fun):

    return fun(num)

def function(num):

    return num**2

result=app(2,function)
print(result)


