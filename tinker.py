import string
from tkinter import *
from random import *
from string import *

ROOT_COLOR = "coral"
COLOR_GRAY = "black"
MAIN_FONT = ("Arial", 14, "bold")
SECONDARY_FONT = ("Times New Roman", 14, "bold")
#
# root = Tk()
# root.title("Distance Convertor")
# # root.resizable(0, 0)
# root.config(bg=ROOT_COLOR)
# root.rowconfigure(0, weight=1)
# root.rowconfigure(1, weight=1)
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)
#
#
# def calculate():
#     user_input = entry.get()
#     result_mtr = float(user_input) * 3.28
#     value_ft.config(text=result_mtr)
#
#     result_cm = float(user_input) * 100
#     value_cm.config(text=result_cm)
#
#
# def pwd_generator():
#     pwd_letter = list(ascii_uppercase + digits + ascii_lowercase + "!@#$%^&*()_-+")
#     shuffle(pwd_letter)
#     new_password = []
#     length = randint(6, 15)
#     for letter in range(length):
#         new_password.append(choice(pwd_letter))
#
#     # print("".join(new_password))
#     pwd_generated = "".join(new_password)
#     pwd_generated_field.config(text=pwd_generated)
#
#
# def copy_text():
#     copied = pwd_generated_field.cget("text")
#     root.clipboard_clear()
#     root.clipboard_append(copied)
#
#
# label_mtr = Label(root, text="Meter", bg=ROOT_COLOR, font=MAIN_FONT)
# entry = Entry(root)
# label_ft = Label(root, text="Feet", bg=ROOT_COLOR, font=MAIN_FONT)
# label_cm = Label(root, text="Centimeter", bg=ROOT_COLOR, font=MAIN_FONT)
# value_ft = Label(root, text="0.00", fg="red", bg=COLOR_GRAY, font=SECONDARY_FONT)
# value_cm = Label(root, text="0.00", fg="red", bg=COLOR_GRAY, font=SECONDARY_FONT)
# button = Button(root, text="Calculate", command=calculate)
#
# label_mtr.grid(row=0, column=0, sticky="W", padx=10)
# entry.grid(row=0, column=1, padx=10, sticky="W", pady=5)
# label_ft.grid(row=1, column=0, sticky="W", padx=10)
# value_ft.grid(row=1, column=1, sticky="w", padx=10, pady=5)
# label_cm.grid(row=2, column=0, sticky="W", padx=10)
# value_cm.grid(row=2, column=1, sticky="w", padx=10, pady=5)
# button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
#
# pwd_generated_field = Label(root, bg=COLOR_GRAY, fg="red", font=SECONDARY_FONT, text="Random Password")
# button_generate = Button(root, text="Generate", command=pwd_generator)
# button_copy = Button(root, text="Copy", command=copy_text)
#
# pwd_generated_field.grid(row=5, column=0, columnspan=2, pady=20)
# button_generate.grid(row=6, column=0, pady=10)
# button_copy.grid(row=6, column=1, pady=10)
#
# root.mainloop()


# **************** #       # ******************* #       # ********************* #      # ******************* #

#
# root = Tk()
# root.title("Calculator")
# root.geometry("330x500")
#
# frame_main = Frame(root)
# frame_main.pack()
#
# frame_top = Frame(frame_main, pady=10)
# frame_top.pack()
# screen = Listbox(frame_top, height=4, width=45)
# screen.grid(column=0, row=0)
# screen.pack()
#
# frame_row_5 = Frame(frame_main)
# frame_row_5.pack()
# button_ac = Button(frame_row_5, text="AC", height=4, width=6)
# button_ac.grid(row=0, column=0, sticky="EWNS")
#
# button_bracket = Button(frame_row_5, text="( )", height=4, width=6)
# button_bracket.grid(row=0, column=1, sticky="EWNS")
#
# button_percentage = Button(frame_row_5, text="%", height=4, width=6)
# button_percentage.grid(row=0, column=2, sticky="EWNS")
#
# button_divide = Button(frame_row_5, text="/", height=4, width=6)
# button_divide.grid(row=0, column=3, sticky="EWNS")
#
# frame_row_4 = Frame(frame_main)
# frame_row_4.pack()
# button_seven = Button(frame_row_4, text="7", height=4, width=6)
# button_seven.grid(row=0, column=0)
#
# button_eight = Button(frame_row_4, text="8", height=4, width=6)
# button_eight.grid(row=0, column=1)
#
# button_nine = Button(frame_row_4, text="9", height=4, width=6)
# button_nine.grid(row=0, column=2)
#
# button_multi = Button(frame_row_4, text="X", height=4, width=6)
# button_multi.grid(row=0, column=3)
#
# frame_row_3 = Frame(frame_main)
# frame_row_3.pack()
# button_four = Button(frame_row_3, text="4", height=4, width=6)
# button_four.grid(row=0, column=0)
#
# button_five = Button(frame_row_3, text="5", height=4, width=6)
# button_five.grid(row=0, column=1)
#
# button_six = Button(frame_row_3, text="6", height=4, width=6)
# button_six.grid(row=0, column=2)
#
# button_minus = Button(frame_row_3, text="-", height=4, width=6)
# button_minus.grid(row=0, column=3)
#
# frame_row_2 = Frame(frame_main)
# frame_row_2.pack()
# button_one = Button(frame_row_2, text="1", height=4, width=6)
# button_one.grid(row=0, column=0)
#
# button_two = Button(frame_row_2, text="2", height=4, width=6)
# button_two.grid(row=0, column=1)
#
# button_three = Button(frame_row_2, text="3", height=4, width=6)
# button_three.grid(row=0, column=2)
#
# button_plus = Button(frame_row_2, text="+", height=4, width=6)
# button_plus.grid(row=0, column=3)
#
# frame_row_1 = Frame(frame_main)
# frame_row_1.pack()
# button_zero = Button(frame_row_1, text="0", height=4, width=6)
# button_zero.grid(row=0, column=0)
#
# button_dot = Button(frame_row_1, text=".", height=4, width=6)
# button_dot.grid(row=0, column=1)
#
# button_back = Button(frame_row_1, text="bksp", height=4, width=6)
# button_back.grid(row=0, column=2)
#
# button_equal = Button(frame_row_1, text="=", height=4, width=6)
# button_equal.grid(row=0, column=3)
#
# root.mainloop()

##########################################################################################################


# import tkinter as tk
#
# root = tk.Tk()
# root.geometry("600x600")
# frame = tk.Frame(root)
# frame.pack(fill=tk.BOTH, expand=True)
#
# button1 = tk.Button(frame, text="Button 1")
# button2 = tk.Button(frame, text="Button 2")
# button3 = tk.Button(frame, text="Button 3")
#
# button1.grid(row=0, column=0, sticky="ew")
# button2.grid(row=0, column=1, sticky="ew")
# button3.grid(row=0, column=2, sticky="ew")
#
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)
# root.columnconfigure(2, weight=1)
#
# root.mainloop()


# word_dictionary = {
#     "hi": "a way to greet",
#     "love": "feelings for other person",
#     "computer": "an electronic device",
#     "fish": "animal that lives in water"
# }
#
# user_input = input("type a word: ")
# if user_input in word_dictionary:
#     meaning = word_dictionary[user_input]
#     print(f"The meaning of '{user_input}' is: {meaning}")
# else:
#     print(f"Sorry the word you entered '{user_input}' is not available"

