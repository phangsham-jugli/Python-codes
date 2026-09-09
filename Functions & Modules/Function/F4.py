#Types of Arguments

#1.Positional arguments
def add(a,b):
    return a+b
result=add(1,2)
print(f'{result}\n')

#2.Default argument
def add2(a,b=12):
    return a+b
result2=add2(2)
print(f'{result2}\n')

#3.keyword argument
def add3(a,b=12,c=10):
    return a+b+c
result3=add3(2,c=15)
print(f'{result3}\n')

#4.Variable length positional argument -*args
def add4(*args):
   print(args,type(args))
   return sum(args)

result4=add4(2,3,4,5)
print(f"{result4}\n")

#5.Variable length keyword arguments
def add5(**kwargs):
   print(kwargs)
   return sum(kwargs.values()) #we use this cause it is dictionaries

result5=add5(a=12,b=33,c=5)
print(result5)



