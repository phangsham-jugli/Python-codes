"""
Write a function sum_numbers(*args) that accepts any number of numbers and returns their sum.
"""
def ad(*args):
    final=sum(args)
    return final

result=ad(10,20,30,40,50,55)

print(result)