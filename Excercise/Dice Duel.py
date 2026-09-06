import random

print("Welcome to the game of rolling a dice!\n")


def game():
    user_1 = 0
    user_2 = 0
    count = 1

    while count <= 6:

        print(f"\nRound {count}")

        user = int(input("User 1 or 2: "))

        choice = input("Press ENTER to continue or Q to quit game: ")

        if choice.lower() == "q":
            print("Game over!")
            break

        elif user == 1:
            marks = random.randint(1, 10)
            user_1 += marks
            print("User 1 rolled:", marks)

        elif user == 2:
            marks = random.randint(1, 10)
            user_2 += marks
            print("User 2 rolled:", marks)

        else:
            print("INVALID")
            break

        count += 1

    print("\nFinal Scores:")
    print("User 1:", user_1)
    print("User 2:", user_2)

    if user_1 > user_2:
        print(f"User 1 Won: {user_1}")
    elif user_2 > user_1:
        print(f"User 2 Won: {user_2}")
    else:
        print("Nobody wins!")

    return user_1, user_2


game()

print("\nGAME OVER")