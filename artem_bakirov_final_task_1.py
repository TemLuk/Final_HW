import random
import keyboard
Player = int(input("Your choice (scissors-1, paper-2, rock-3, lizard-4, spock-5)? "))
Computer = random.randint(1, 5)


def player_choice():
    if Player == 1:
        print("Player: scissors ")
    if Player == 2:
        print("Player: paper")
    if Player == 3:
        print("Player: rock")
    if Player == 4:
        print("Player: lizard")
    if Player == 5:
        print("Player: spock")


def comp_chice():
    if Computer == 1:
        print("Computer: scissors ")
    if Computer == 2:
        print("Computer: paper")
    if Computer == 3:
        print("Computer: rock")
    if Computer == 4:
        print("Computer: lizard")
    if Computer == 5:
        print("Computer: spock")


def winner():
    if Player == Computer:
        win = 0
    if Player == 1 and Computer == 2:
        win = 1
    if Player == 1 and Computer == 3:
        win = 2
    if Player == 1 and Computer == 4:
        win = 1
    if Player == 1 and Computer == 5:
        win = 2
    if Player == 2 and Computer == 1:
        win = 2
    if Player == 2 and Computer == 3:
        win = 1
    if Player == 2 and Computer == 4:
        win = 2
    if Player == 2 and Computer == 5:
        win = 1
    if Player == 3 and Computer == 1:
        win = 1
    if Player == 3 and Computer == 2:
        win = 2
    if Player == 3 and Computer == 4:
        win = 1
    if Player == 3 and Computer == 5:
        win = 2
    if Player == 4 and Computer == 1:
        win = 2
    if Player == 4 and Computer == 2:
        win = 1
    if Player == 4 and Computer == 3:
        win = 2
    if Player == 4 and Computer == 5:
        win = 1
    if Player == 5 and Computer == 1:
        win = 1
    if Player == 5 and Computer == 2:
        win = 2
    if Player == 5 and Computer == 3:
        win = 1
    if Player == 5 and Computer == 4:
        win = 2
    if win == 0:
        print("Draw!")
    if win == 1:
        print("Player WIN!")
    if win == 2:
        print("Computer WIN!")


while True:
    try:
        player_choice()
    except ValueError as e:
        print(f"Invalid selection, {e}")
        continue

    comp_chice()
    winner()

    play_again = input("Play again? (y/n): ")
    if play_again.lower() == "y":
        keyboard.send('shift+F10')
    else:
        break
