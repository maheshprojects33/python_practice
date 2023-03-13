# def main():
#     print(f"Welcome to EMI Calculator \n")
#
#     principle = float(input("Enter Your Principle Amount: "))
#     interest_rate = float(input("Enter Your Interest Rate: "))
#     duration = float(input("Enter Duration in Year: "))
#
#     r = interest_rate / 12 / 100
#     n = duration * 12
#     p = principle
#
#     emi = p * r * (1 + r) ** n / ((1 + r) ** n - 1)
#
#     print(round(emi, 3))
#
# main()

import random
import string

character = list(string.ascii_lowercase + string.digits + string.ascii_letters + string.punctuation + string.ascii_uppercase)


def generate_password():
    password_length = int(input("How long password do you want to generate: "))

    random.shuffle(character)

    password = []

    for x in range(password_length):
        password.append(random.choice(character))

    random.shuffle(password)

    password = "".join(password)

    print(password)


while True:
    option = input("Do you want to Generate Random Password y/n: ").lower()
    if option == "y":
        generate_password()
    elif option == "n":
        print("See you soon!!!")
        break
    else:
        print("Invalid option ")
        continue
