import re
Uemail=input("Enter email:")

ptr=r"^[A-Za-z][\w._]+[@][a-z]+[.]com$"

if re.fullmatch(ptr,Uemail):
    print("Valid")
else:
    print("invalid")