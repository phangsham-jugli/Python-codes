"""
Function + map()
Create a normal function square(n) and use it with map() to find the squares of:

[2, 4, 6, 8, 10]
"""
def sqr(n):
    square=n*n
    return square

num=[2, 4, 6, 8, 10]

result=map(sqr,num)
print(list(result))