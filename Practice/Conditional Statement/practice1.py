#Q1.Largest of Three Numbers
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if a>b and c:
    print(f"Largest number is :{a}")
elif b>a and c:
    print(f"Largest number is:{b}")
else:
    print(f"Largest number is :{c}")
    