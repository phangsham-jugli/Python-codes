import re

"""
Password validation ⭐
Password must contain:
- at least one uppercase letter
- at least one lowercase letter
- at least one digit
- at least one special character
- minimum 8 characters
"""

psswrd = input("Enter your password: ")

ptr = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$"

rest = re.fullmatch(ptr, psswrd)

if rest:
    print("Valid")
else:
    print("Invalid")