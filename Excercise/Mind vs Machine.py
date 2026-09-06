import random
print("Guess the number between 1 to 30!\n")
count=1
secret_number=random.randint(1,30)
while count<=10:
    comp = random.randint(1, 30)
    user = int(input("Enter the number:"))
    print(f"Computer number:{comp}\n")
    if user ==secret_number:
        print("Congrats you won 🎉!")
        break
    elif comp== secret_number:
        print("Computer won!")
        break
    elif user<secret_number:
        print("Enter Higher Number!")
        print(f"Remaining attempts:{11-count}")
    else:
        print("Enter Lower Number!")
        print(f"Remaining attempts:{10 - count}")

    count +=1
if count>10:
    print(f"Both loses 👎! secret number was:{secret_number}")

print("Game over (❁´◡`❁)")
