welcome_msg = "########### WELCOME TO MD's MART ###########"
welcome_menu = "\n********** Below is our MENU for your SHOPPING **********"
name = input("Please enter your name: ").title()
name_update = name
salutation = input("How should I salute you Mr/Mrs/Ms: ").lower()
while True:
    if salutation == "mr":
        name_update = "Mr." + name
        print(f"Hello {name_update}")
        break
    elif salutation == "mrs":
        name_update = "Mr." + name
        print(f"Hello {name_update}")
        break
    elif salutation == "ms":
        name_update = "Mr." + name
        print(f"Hello {name_update}")
        break
    else:
        print("Didn't Understand, Try Again!!>")
        continue

print(f"********** Welcome to MD's Mart **********")
input("Press Enter To Continue.....")
print(welcome_menu)


shopping_list = {}
shopping_cart = {}


def menu():
    my_file = open("shopping.txt", "r")
    first_line = my_file.readline()
    print(first_line)
    available_menu_list = my_file.readlines()
    # print(available_menu_list)
    my_file.close()

    for item in available_menu_list:
        item_name = item.split()[0]
        item_price = item.split()[1]
        print(f"{item_name}: {item_price}")
        shopping_list.update({item_name: float(item_price)})
    # print(shopping_list)


menu()

while True:
    total_bill = 0
    user_choice = input(f"Do you want to proceed with the shopping ...... y/n: ").lower()
    while user_choice == "y":
        add_item = input("Select an Item to add in your cart: ").title()
        while add_item in shopping_list:
            add_qty = input(f"How many of '{add_item.upper()}' to you want to add in your cart: ")

            shopping_cart.update({add_item: {"quantity": add_qty, "subTotal": shopping_list[add_item] * float(
                add_qty)}})

            total_bill += shopping_cart[add_item]["subTotal"]

            loop_break = False

            if add_qty.isdigit():
                while True:
                    add_qty = input("Do you want to add more items? y/n: ")
                    if add_qty == "y":

                        loop_break = True
                        break
                    elif add_qty == "n":
                        print(f"\n\n*******--Bill Summary--******* \nItems     Quantity     Price")

                        for key in shopping_cart:
                            space_need_to_qty = 10 - len(key)
                            space_need_to_price = 9 - len(shopping_cart[key]['quantity'])

                            print(f"{key}    {' ' * space_need_to_qty}{shopping_cart[key]['quantity']}"
                                  f"{' ' * space_need_to_price}{shopping_cart[key]['subTotal']}")
                        print("-" * 30)
                        print(f"Your Total Bill is: {total_bill}")
                        print("-" * 30)
                        print(f"Thank You for Shopping with us '{name_update}'")

                        quit()
                    else:
                        print(f"Invalid Choice '{name_update}', Please try again: ")
                        continue
            else:
                print(f"Quantity Should be a Number '{name_update}'!! ")
                continue
            if loop_break:
                break
        else:
            print("Item not in our list!!! Please select again: ")
            menu()
            # continue
    if user_choice == "n":
        print(f"Thank You for Shopping with us '{name_update}'")
        break
    else:
        print(f"Please Input Valid Choice '{name_update}': ")
        continue


