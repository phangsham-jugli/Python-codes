#To Reverse the number
num=int(input("Enter the number:"))
reverse=0
newn=0
while num>0:
    a=num%10
    reverse=reverse*10+a
    num=num//10

print(f"The reverse of number:{reverse}")
