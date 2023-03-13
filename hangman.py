import random
from words import words

secret = random.choice(words)
print('!!! Welcome to Hangman Game !!! \n Guess the below word:')

display = ["_"] * len(secret)
lives = 6
word_guessed = []

while lives > 0:
    print(" ".join(display))
    guess = input("Guess: ")

    if guess in word_guessed:
        print("Already Guessed, Try Again:")
        word_guessed.remove(guess)
    elif guess in secret:
        for i in range(len(secret)):
            if secret[i] == guess:
                display[i] = guess
    elif guess not in secret:
        lives -= 1
        if lives == 1:
            print("Its a last chance take your time to guess:")
        elif lives == 0:
            print("You have wasted your last chance!! Game Over")
            print(f'The Secret Word is: "{secret}"')
        else:
            print(f"Wrong Guess, Try Again you have {lives} lives remaining")

    word_guessed.append(guess)
    print(f"Your Guess List is: {word_guessed}")

    if "_" not in display:
        print(f"Bravo!! You got the secret word: {secret}")
        break
