#Returning value form function
#1
def OE(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

n=int(input("Enter a number:"))
result=OE(n) #assigning return to result
print(f"{n} is {result}")
print("\n")

#Returning multiple value
#2
def arithmetic(num1,num2):
    sm=num1+num2
    sub=num1-num2
    mul=num1*num2
    div=num1/num2
    return sm,sub,mul,div

n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))

val1,val2,val3,val4=arithmetic(n1,n2)

print(f"sum of {n1}+{n2}={val1}")
print(f"substraction of {n1}-{n2}={val2}")
print(f"Multiplication of {n1}*{n2}={val3}")
print(f"division of {n1}/{n2}={round(val4,2)}")
