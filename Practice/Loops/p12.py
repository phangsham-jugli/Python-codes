"""To check prime number of not"""
n=int(input("Enter a number:"))
nt=2
count=0
if n <=1:
    print("It is not an prime")
else:
    for i in range(2,n):
        if n%i==0:
            count+=1


if count==0:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")




