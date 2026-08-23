
"""
Area of triangle if we know three sides a, b, c

s = (a + b + c) / 2
area = square root of s(s-a)(s-b)(s-c)
"""

a = int(input("Enter first side of triangle: "))
b = int(input("Enter second side of triangle: "))
c = int(input("Enter third side of triangle: "))

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
    #We use 0.5 because square root = power 1/2 = 0.5

    print("Area of triangle is", round(area, 2))
else:
    print("These sides cannot form a triangle.")