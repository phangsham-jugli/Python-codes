"""
map() + lambda
Given:

names = ["ram", "john", "alex", "sam"]

Use map() and lambda to convert every name into uppercase.
"""
names = ["ram", "john", "alex", "sam"]

fun=lambda x:x.upper()

uppercase=map(fun,names)
print(list(uppercase))