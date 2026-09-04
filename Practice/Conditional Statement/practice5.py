#Q5.Character Type
a=input("Enter the character:")

if a.isdigit():
    print("Character is Digit!")
elif a.isupper():
    print("Character is upper case")
elif a.islower():
    print("Character is lower case")
else:
    print("It is Special Character")