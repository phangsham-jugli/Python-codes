import random

print("Welcome to the game of rolling a dice!")


def roll_a_die():
    while True:
        choice = input("Choose Enter to Continue or Q to quit: ")

        if choice == '':
            print(random.randint(1, 6))
        else:
            break


roll_a_die()

print("Quit game!")
print("\n")

print("Do you want to play again?")
ip = input("Enter to Continue or Q to Exit: ")

if ip == '':
    roll_a_die()