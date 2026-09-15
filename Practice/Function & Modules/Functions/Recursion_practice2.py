#To print number from 1 to n
def new(n):
    if n==0:
        return
    else:
        new(n-1)
        print(n)

new(5)