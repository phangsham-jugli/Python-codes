import re

uname=input("Enter your user name:")
prt=r"^[A-Za-z][A-Za-z\d_.]{4,14}$"

if re.fullmatch(prt,uname):
    print("Valid")
else:
    print("Invalid")