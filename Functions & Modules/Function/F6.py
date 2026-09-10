#LOCAL AND GLOBAL VARIABLE
n=1 #Global variable

def fn():
    n=5 #Local variable
    print("This is inside function value of n:",n)

fn()

print("This outside function value of n:",n)