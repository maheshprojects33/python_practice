import random
from words import words

four_letter_words = [word for word in words if len(word) == 4 and len(set(word)) == 4]
secret = random.choice(four_letter_words)
print("Welcome to the Cow N Bull game")
print("Guess the word of 4 Letters _ _ _ _")
guessed_word = []
print(secret)


def rules():
    if user_guess in guessed_word:
        print("Already Guessed!!")
        guessed_word.remove(user_guess)
        return
    elif len(user_guess) != 4:
        print("Words Should be of 4 characters")
        return


def play():
    cow_count = 0
    bull_count = 0
    for i in range(len(secret)):
        if user_guess[i] == secret[i]:
            bull_count += 1
        elif user_guess[i] in secret:
            cow_count += 1
    if len(user_guess) != len(set(user_guess)):
        print("Letters should not repeat")
        return
    print("cow:", cow_count)
    print("bull:", bull_count)
    guessed_word.append(user_guess)


while True:
    user_guess = input("Guess the word: ")
    rules()
    if len(user_guess) != len(secret):
        continue
    play()
    if guessed_word:
        print("Words You have Guessed:", guessed_word)
    if user_guess == secret:
        print("You Win")
        break


# from tkinter import *
#
# FONT_MAIN = ("Arial", 14, "bold")
# FONT_SECONDARY = ("Comic Sens", 12, "bold")
#
# root = Tk()
# root.title("Cow N Bull")
# root.geometry("400x600")
# root.resizable(False, False)
#
#
# def add_to_guessed():
#     pass
#
#
# frame_main = Frame(root, bg="red")
# frame_main.pack(expand=True, fill="both", pady=10, padx=10)
#
# frame_top = Frame(frame_main, bg="yellow")
# frame_top.pack(fill="both")
# frame_top.columnconfigure(0, weight=1)
# frame_top.columnconfigure(1, weight=1)
# frame_top.columnconfigure(2, weight=1)
# # frame_top.rowconfigure(0, weight=1)
#
# dash_for_guess = Label(frame_top, text="\u2014 \u2014 \u2014 \u2014", bg="yellow")
# user_guess_entry = Entry(frame_top, width=17)
# button_submit = Button(frame_top, text="Submit", command=add_to_guessed)
#
# dash_for_guess.grid(row=0, column=0, padx=5)
# user_guess_entry.grid(row=0, column=1, padx=5)
# button_submit.grid(row=0, column=2, padx=5)
#
# frame_center = Frame(frame_main, bg="green", height=400)
# frame_center.pack(expand=True, fill="both")
# frame_center.columnconfigure(1, weight=1)
# frame_center.columnconfigure(2, weight=1)
# # frame_center.rowconfigure(0, weight=1)
#
# user_guessed_words = Label(frame_center, text="Guessed Words List", font=FONT_SECONDARY, bg="green")
# guessed_cow = Label(frame_center, text="COW", font=FONT_SECONDARY, bg="green")
# guessed_bull = Label(frame_center, text="BULL", font=FONT_SECONDARY, bg="green")
#
# user_guessed_words.grid(row=0, column=0, sticky=N)
# guessed_cow.grid(row=0, column=1, sticky=N)
# guessed_bull.grid(row=0, column=2, sticky=N)
#
# frame_bottom = Frame(frame_main, bg="blue", height=50)
# frame_bottom.pack()
# frame_bottom.rowconfigure(0, weight=1)
#
# message = Label(frame_bottom, text="This is dummy text will replace by messages", font=FONT_SECONDARY)
# message.grid()
#
# root.mainloop()
