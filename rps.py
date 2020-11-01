import random
import time

def play():
    user = input("\n\nWhat is your choice?\nEnter 'r' for rock, 'p' for paper and 's' for scissors.\nPress the enter key to exit from the game.\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print("Ah huh?")
        return "You and the computer have both chosen \'{}\'. It is a tie.".format(computer)

    if won(user, computer):
        print("Yaaayy!")
        return "You have chosen \'{}\' and the computer has chosen \'{}\'. You have won! XD".format(user, computer)

    if lost(user, computer):
        print("Opsss!")
        return "You have chosen \'{}\' and the computer has chosen \'{}\'. You have lost. :/".format(user, computer)

    if len(user) < 1:
        print("Closing...")
        time.sleep(5)
        exit()

    if (user != 'r' or 'p' or 's'):
        return "You have entered \'{}\' and it is not a valid input. Please enter 'r' or 'p' or 's' to play the game.".format(user)


def won(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    else:
        return False

def lost(player, opponent):
    if (player == 'r' and opponent == 'p') or (player == 'p' and opponent == 's') or (player == 's' and opponent == 'r'):
        return True
    else:
        return False

i = 5
while (i<10):
    print(play())
