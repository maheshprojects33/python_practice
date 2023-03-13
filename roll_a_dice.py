import random
from bullet import Bullet

dot = "\u25CF"
top_left = "\u231c"
top_right = "\u231d"
bottom_left = "\u231e"
bottom_right = "\u231f"


def dice_face_1():
    print(f"""{top_left}          {top_right}

     {dot}

{bottom_left}          {bottom_right}
    """)


def dice_face_2():
    print(f"""{top_left}          {top_right}
        {dot}

   {dot}
{bottom_left}          {bottom_right}
    """)


def dice_face_3():
    print(f"""{top_left}          {top_right}
        {dot}
     {dot}
  {dot}
{bottom_left}          {bottom_right}
    """)


def dice_face_4():
    print(f"""{top_left}          {top_right}
  {dot}     {dot}

  {dot}     {dot}
{bottom_left}          {bottom_right}
    """)


def dice_face_5():
    print(f"""{top_left}          {top_right}
  {dot}     {dot}
     {dot}
  {dot}     {dot}
{bottom_left}          {bottom_right}
    """)


def dice_face_6():
    print(f"""{top_left}          {top_right}
  {dot}     {dot}
  {dot}     {dot}
  {dot}     {dot}
{bottom_left}          {bottom_right}
    """)


while True:
    user_input = input("Do you want to roll dice y/n: ")
    if user_input == "y":
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        if dice_one == 1 or dice_two == 1:
            dice_face_1()

        if dice_one == 2 or dice_two == 2:
            dice_face_2()

        if dice_one == 3 or dice_two == 3:
            dice_face_3()

        if dice_one == 4 or dice_two == 4:
            dice_face_4()

        if dice_one == 5 or dice_two == 5:
            dice_face_5()

        if dice_one == 6 or dice_two == 6:
            dice_face_6()
    else:
        print("See You Again!!! ")
        break
