#to check even or odd using function

def check(num):
    if num%2==0:
        return True
    else:
        return False

n=int(input("Enter the number:"))
result=check(n)
if result==True:
    print(f"{n} is even")
else:
    print(f"{n} is odd")