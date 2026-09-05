#While Loop
#To print all natural number from 1 to 10
num=1
while num<11:
    print(num)
    num=num +1
print("Out of loop\n")

#infinite while loop
correct="Admin121"

while True:
    password=input("Enter the Password:")
    if password==correct:
        print("Password is correct!")
        break
    else:
        print("Try again!")

print("Logged in")
