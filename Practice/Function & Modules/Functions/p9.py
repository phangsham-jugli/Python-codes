"""
Write a function that demonstrates positional arguments, keyword arguments, and default arguments.
"""

def home(Biscuit,Milk,Rice='1kg'):
    print(f'Biscuit:{Biscuit}|MILK:{Milk}|Rice:{Rice}')

b=input("Enter the quantity of Biscuit:")

home(b,Milk='2ltr')

