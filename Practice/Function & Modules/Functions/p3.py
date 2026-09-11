#To write function of addition

def add(a,b):
    ad=a+b
    return ad

a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
result=add(a,b)
print(f"Sum of {a}+{b}={result}")