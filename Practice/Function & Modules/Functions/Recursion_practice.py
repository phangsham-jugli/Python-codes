#To add number 1 to n
def add(n):
    if n==0:
        return 0
    else:
        return n + add(n - 1)



num=int(input("Enter the number:"))
result=add(num)
print(result)