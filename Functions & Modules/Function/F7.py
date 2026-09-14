#Function as an argument
def add(number):
    return number + 1

def sqr(number):
    return number **2

num=int(input("Enter a number:"))
result=sqr(add(num))

print(f"Output is:{result}")

