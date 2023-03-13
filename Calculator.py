# import random
#
#
# def guess(x):
#     random_number = random.randint(1, x)
#     user_guess = 0
#     total_guess = 6
#     while user_guess != random_number and total_guess > 0:
#         user_input = int(input(f"Guess the number between 1 to {x}: "))
#         total_guess -= 1
#         if user_input == random_number:
#             print("you win")
#             break
#         elif user_input < random_number:
#             print("Your guess should be higher")
#             print(f"Your Remaining Chance to guess is {total_guess}")
#         else:
#             print("Your guess should be lower")
#     print(f"The Secret Number is: {random_number}")
#
# guess(100)
# def computer_guess(x):
#     secret_number = 3
#     low = 1
#     high = x
#     feedback = ""
#     while feedback != "c":
#         if low != high:
#             guess = random.randint(low, high)
#         else:
#             guess = low
#
#         feedback = input(f"Is {guess} too high (h), too low(l), correct (c): ").lower()
#         if feedback == "h":
#             high = guess - 1
#         elif feedback == "l":
#             high = guess + 1
#     print(f"The computer guess {guess} is correct")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # class Person:
# #     def __init__(self):
# #         print("""Welcome to Simple Calculator
# #         what do you want to do
# #         1. addition
# #         2. subtraction
# #         3. multiplication
# #         4. quit/exit""")
# #         self.option = input("Please make a selection: ")
# #         if self.option == "1":
# #             print("You have selected 'Addition'")
# #             numbers = self.user_input()
# #             self.addition(numbers)
# #         elif self.option == "2":
# #             print("You have selected 'Subtraction'")
# #             self.f_num, self.s_num = self.user_input()
# #             self.subtraction(self.f_num, self.s_num)
# #         elif self.option == "3":
# #             print("You have selected 'Multiplication'")
# #             numbers = self.user_input()
# #             self.multiplication(numbers)
# #         elif self.option == "4":
# #             print("Thanks for using my program")
# #         else:
# #             print("Make a valid selection")
# #
# #     def user_input(self):
# #         numbers = []
# #         while True:
# #             num = input("Enter Number: ")
# #             if num.lower() == "=":
# #                 break
# #             numbers.append(int(num))
# #         return numbers
# #
# #     def addition(self, numbers):
# #         result = sum(numbers)
# #         print(f"The result is {result}")
# #
# #     def subtraction(self, f_num, s_num):
# #         result = f_num - s_num
# #         print(result)
# #
# #     def multiplication(self, numbers):
# #         result = 1
# #         for num in numbers:
# #             result *= num
# #         print(result)
# #
# #
# # p = Person()
import tinker as tk

COLOR_LIGHT_GRAY = "#F5F5F5"
COLOR_LABEL = "#25265E"
COLOR_WHITE = "#FFFFFF"
COLOR_OFF_WHITE = "#F8FAFF"
COLOR_LIGHT_BLUE = "#CCEDFF"

FONT_SMALL = ("Arial", 16)
FONT_LARGE = ("Arial", 40, "bold")
FONT_DIGITS = ("Arial", 24, "bold")
FONT_DEFAULT = ("Arial", 20)

COLOR_RED = "red"
COLOR_YELLOW = "yellow"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x550")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_label()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            ".": (4, 1), 0: (4, 2)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.button_frame = self.create_button_frame()
        self.button_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_clear_buttons()
        self.create_equal_buttons()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=COLOR_YELLOW)
        frame.pack(expand=True, fill="both")
        return frame

    def create_button_frame(self):
        frame = tk.Frame(self.window, bg=COLOR_RED)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=COLOR_LIGHT_GRAY,
                               fg=COLOR_LABEL, padx=24, font=FONT_SMALL)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=COLOR_LIGHT_GRAY,
                         fg=COLOR_LABEL, padx=24, font=FONT_LARGE)
        label.pack(expand=True, fill="both")

        return total_label, label

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_total_label()
        self.update_label()

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()

        self.current_expression = str(eval(self.total_expression))

        self.total_expression = ""
        self.update_label()


    def append_operation(self, operation):
        self.current_expression += operation
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg=COLOR_WHITE, fg=COLOR_LABEL, font=FONT_DIGITS,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text=symbol, bg=COLOR_OFF_WHITE, fg=COLOR_LABEL, font=FONT_DEFAULT,
                               borderwidth=0, command= lambda x= operator: self.append_operation(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_clear_buttons(self):
        button = tk.Button(self.button_frame, text="AC", bg=COLOR_OFF_WHITE, fg=COLOR_LABEL, font=FONT_DEFAULT,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

    def create_equal_buttons(self):
        button = tk.Button(self.button_frame, text="=", bg=COLOR_LIGHT_BLUE, fg=COLOR_LABEL, font=FONT_DEFAULT,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)




    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
