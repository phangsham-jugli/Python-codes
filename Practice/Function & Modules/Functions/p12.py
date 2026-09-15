"""1. Function as an argument
Write a function calculate(a, b, operation) where operation is another function. Use it to perform addition and multiplication.
"""

def calculate(a,b,operation):
    return operation(a,b)


def add(a, b):

        return a + b

def multi(a, b):

        return a * b

result1=calculate(1,2,add)
result2=calculate(1,2,multi)

print(f"{result1}")
print(f"{result2}")