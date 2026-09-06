print("guess the Secret number between 1 and 50!")
Secret_number=45

count=1
while count<=10:
    user=int(input("Enter the number:"))
    if user==Secret_number:
        print("Congrats🎉!")
        break
    else:
        if user<Secret_number:
            print("Enter Higher number!")
        else:
            print("Enter Lower number!")
    count+=1

print("Game Over!")