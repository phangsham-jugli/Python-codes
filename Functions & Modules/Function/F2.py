#function with argument
def check(num):
    if num%2==0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

count=0
while count<4:
    n=int(input("Enter the number:"))
    check(n)
    count +=1

print("\n") #out of loop

#To add two number using function
def add(num1,num2):
    sum=num1+num2
    return sum #returning the value

n1=int(input("Enter the 1st number:"))
n2=int(input("Enter the 2nd number:"))
print(f"sum of n1 and n2 is:{add(n1,n2)}")