#To count the digits
num=int(input("Enter the number:"))
count=0
while num>0:
    num=num//10
    count +=1

print(f"The total digit in a number is:{count}")