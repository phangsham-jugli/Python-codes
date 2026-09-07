#To find the Factorial
num=int(input("Enter the number to find it factorial:"))

fact=1
for i in range(1,num+1):
    fact =fact*i

print(f"Factorial of {num} is:{fact}")