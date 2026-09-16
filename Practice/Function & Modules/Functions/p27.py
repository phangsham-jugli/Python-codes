"""
Math module
Import the math module and write a program to find:

Square root of a number
Power of a number
Factorial of a number
Natural logarithm (log base e)
Sine of a number in radians
"""
import math

a=int(input("Enter a number:"))
sqr=math.sqrt(a)
power=math.pow(a,3)
log=math.log(a,10)
sine=math.sin(a)

print(f"square root of number:{sqr}\n"
      f"power of number:{power}\n"
      f"log of number:{log}\n"
      f"sine of number:{sine}\n")