"""To check Palindrome using loop"""
num=int(input("Enter a number:"))
orginal=num
rev=0
while num>0:
    a=num%10
    rev=rev*10+a
    num=num//10


if rev==orginal:
     print(f"{orginal} is Palindrome")
else:
     print(f"{orginal} is Not Palindrome")

