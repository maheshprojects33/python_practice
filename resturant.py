def welcome():
    print("""!!! Welcome To ABC Cafe' !!!
    Self-Ordering Machine:
    ---------- Our Menu ----------
    1. Coffee - 100           2. Tea - 50
    3. Pizza - 175            4. Burger - 170
    5. Cold Drinks - 85       6. Momo - 130
    """)


class Restaurant:
    def __init__(self):
        self.menu = []
        self.qty = 0
        self.total = 0

    def user_order(self, order):
        self.menu.append(order)
        self.total += self.menu[order]

    def print_bill(self):
        for order in self.menu:
            print(f"{order} : {self.menu[order]}")

welcome()
rest = Restaurant()
user_order = input("What would you like to have today: ")
rest.user_order(user_order)
# user_qty = int(input("How Many: "))


















# def welcome():
#     print("""!!! Welcome To ABC Cafe' !!!
#     Self-Ordering Machine:
#     ---------- Our Menu ----------
#     1. Coffee           2. Tea
#     3. Pizza            4. Burger
#     5. Cold Drinks      6. Momo
#     """)
#
#
# def order():
#     user_selection = set()
#     grand_total = 0
#     total_qty = 0
#     name = ""
#     price = 0
#     while True:
#         user_order = input("What would you like to have today: ")
#         if user_order == "1":
#             name = item_name.get('1')
#             price = int(item_price.get("Coffee"))
#
#             user_qty = input(f"How many of {name} do you want to order: ")
#
#             total_qty += int(user_qty)
#             total_amount = total_qty * price
#             user_selection.add(name)
#             total_amount = grand_total
#
#             user_order_add = input("Would you like to have more 'y' for 'yes' 'n' for 'no': ")
#             if user_order_add == "y":
#                 continue
#             else:
#                 print(f"Thank you for your order {user_name}")
#                 print(f"""Your orders are:
# {name}: {total_qty}: {total_amount}
# {user_selection}""")
#                 break
#         elif user_order == "2":
#             name = item_name.get('2')
#             price = int(item_price.get("Tea"))
#
#             user_qty = input(f"How many of {name} do you want to order: ")
#
#             total_qty += int(user_qty)
#             total_amount = total_qty * price
#             user_selection.add(name)
#
#             user_order_add = input("Would you like to have more 'y' for 'yes' 'n' for 'no': ")
#             if user_order_add == "y":
#                 continue
#             else:
#                 print(f"Thank you for your order {user_name}")
#                 print(f"""Your orders are:
#             {name}: {total_qty}: {total_amount}
# {user_selection}""")
#                 break
#         elif user_order == "3":
#             name = item_name.get('3')
#             price = int(item_price.get("Pizza"))
#
#             user_qty = input(f"How many of {name} do you want to order: ")
#
#             total_qty += int(user_qty)
#             total_amount = total_qty * price
#             user_selection.add(name)
#
#             user_order_add = input("Would you like to have more 'y' for 'yes' 'n' for 'no': ")
#             if user_order_add == "y":
#                 continue
#             else:
#                 print(f"Thank you for your order {user_name}")
#                 print(f"""Your orders are:
#             {name}: {total_qty}: {total_amount}
# {user_selection}""")
#                 break
#         elif user_order == "4":
#             name = item_name.get('4')
#             price = int(item_price.get("Burger"))
#
#             user_qty = input(f"How many of {name} do you want to order: ")
#
#             total_qty += int(user_qty)
#             total_amount = total_qty * price
#             user_selection.add(name)
#
#             user_order_add = input("Would you like to have more 'y' for 'yes' 'n' for 'no': ")
#             if user_order_add == "y":
#                 continue
#             else:
#                 print(f"Thank you for your order {user_name}")
#                 print(f"""Your orders are:
#             {name}: {total_qty}: {total_amount}
# {user_selection}""")
#                 break
#         elif user_order == "5":
#             name = item_name.get('5')
#             price = int(item_price.get("Cold Drinks"))
#
#             user_qty = input(f"How many of {name} do you want to order: ")
#
#             total_qty += int(user_qty)
#             total_amount = total_qty * price
#             user_selection.add(name)
#
#             user_order_add = input("Would you like to have more 'y' for 'yes' 'n' for 'no': ")
#             if user_order_add == "y":
#                 continue
#             else:
#                 print(f"Thank you for your order {user_name}")
#                 print(f"""Your orders are:
#             {name}: {total_qty}: {total_amount}
# {user_selection}""")
#                 break
#         elif user_order == "6":
#             name = item_name.get('6')
#             price = int(item_price.get("Momo"))
#
#             user_qty = input(f"How many of {name} do you want to order: ")
#
#             total_qty += int(user_qty)
#             total_amount = total_qty * price
#             user_selection.add(name)
#
#             user_order_add = input("Would you like to have more 'y' for 'yes' 'n' for 'no': ")
#             if user_order_add == "y":
#                 continue
#             else:
#                 print(f"Thank you for your order {user_name}")
#                 print(f"""Your orders are:
#             {name}: {total_qty}: {total_amount}
# {user_selection}""")
#                 break
#
# item_name = {
#     "1": "Coffee",
#     "2": "Tea",
#     "3": "Pizza",
#     "4": "Burger",
#     "5": "Cold Drinks",
#     "6": "Momo"
# }
# item_price = {
#     "Coffee": 100,
#     "Tea": 50,
#     "Pizza": 175,
#     "Burger": 170,
#     "Cold Drinks": 85,
#     "Momo": 130
# }
# welcome()
# user_name = input("Please Enter Your Name: ")
# order()
#
