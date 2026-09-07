#To count how many positive of negative numbers

positive=0
negative=0

num=[]

for i in range(10):
    n=int(input(f"Enter the {i+1} number:"))
    num.append(n)

    if n<0:
        negative +=1
    else:
        positive +=1

print("Positive numbers:",positive)
print("Negative numbers:",negative)