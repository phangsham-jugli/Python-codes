#to find the sum of digits
num=int(input("Enter a number:"))
sum=0

while num>0:
    a=num%10
    sum +=a
    num=num//10

print(f"Sum of digit is:{sum}")