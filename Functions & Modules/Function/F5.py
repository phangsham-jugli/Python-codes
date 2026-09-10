#RECURSIVE Function
#factorial of 4 using for loop
def facto(num):
    fact = 1
    while num>=1:
        fact*=num
        num-=1

    return fact

result=facto(4)
print(result)

#factorial of 5 using recursive function
def ft(n):
    if n==1:
        return 1
    else:
        factr=n*ft(n-1)
    return factr
print(ft(5))



