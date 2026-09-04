#Q9.Simple Login System ⭐
# Ask the user for a username and password.
# Use:
# username = admin
# password = 1234

name=input("Enter user name:")
passw=int(input("Enter password:"))
if name=="admin" and passw==1234:
    print("Login Successfully!")
else:
    print("Invalid username and password")
