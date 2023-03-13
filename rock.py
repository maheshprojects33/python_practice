import random


# computer wins = u>r c>p, u>p c>r, u>s, c>r
# you wins = u>r c>s, u>p c>s, u>s c>p

def play():
    user = input("r for rock p for peper s for scissor: ").lower()
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        print(f"You have selected: {user}\nComputer have selected: {computer}")
        return "Draw"
    elif is_win(user, computer):
        print(f"You have selected: {user}\nComputer have selected: {computer}")
        return "You Win"
    elif is_valid(user):
        return "Invalid Input"
    else:
        print(f"You have selected: {user}\nComputer have selected: {computer}")
        return "You Lost"


def is_win(user, computer):
    if (user == "r" and computer == "s") or (user == "p" and computer == "s") or (user == "s" and computer == "p"):
        return True


def is_valid(user):
    if user not in ["r", "p", "s", "e"]:
        return True


while True:
    print("""Welcome to Rock Paper Scissor Game
    1. Play
    2. Exit""")

    user_selection = input("Make your selection: ")
    if user_selection == "1":
        print(play())
    elif user_selection == "2":
        print("Thanks for Playing")
        break
    else:
        print("Invalid Selection")
