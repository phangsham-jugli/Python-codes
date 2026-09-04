#Q7. Triangle Type ⭐
# Take three sides of a triangle and determine whether it is:
# Equilateral
# Isosceles
# Scalene

a=float(input("Enter a side of triangle:"))
b=float(input("Enter b side:"))
c=float(input("Enter c side:"))

if a==b==c:
    print("Equilateral triangle")
elif a==b or a==c or b==c:
    print("Isosceles triangle")
else:
    print("Scalene")