total_balance = 10000
total_withdraw = 0
account_pin = "4516"
user_name = "Mahesh Dangol"


def choice_main_menu(name):
    print(f"Welcome Back Mr.{user_name}")
    print("""
    1. Balance Inquiry      2. Deposit Cash
    3. Withdrawal Amount    4. Fast Cash
    5. Change Your Pin      6. Pay Amount
    7. Exit""")

    menu_selection = input("Please Choose Your Option: ")
    if menu_selection == "1":
        choice_balance()
        input("Press any key to continue...: ")
        choice_main_menu(user_name)
    elif menu_selection == "2":
        choice_deposit()
    elif menu_selection == "3":
        choice_withdraw()
    elif menu_selection == "4":
        choice_fast_cash()
    elif menu_selection == "5":
        choice_change_pin()
    elif menu_selection == "6":
        choice_pay_amount()
    elif menu_selection == "7":
        choice_exit()
    else:
        print("Invalid Selection!! ")
        choice_main_menu(user_name)


def choice_balance(print_balance=True):
    print("Balance Information:")
    global total_balance
    if print_balance:
        print(f"Your Total Balance: {total_balance}")
    return total_balance


def choice_deposit():
    print("Cash Deposit")
    while True:
        user_deposit = input("Enter the amount you want to deposit: ")
        if user_deposit.isdigit():
            global total_balance
            cash_on_machine = input(f"Insert Cash Rs.{user_deposit}/- on the Machine and press Enter: ")
            total_balance = choice_balance(print_balance=False)
            total_balance += int(user_deposit)
            print(f"Your New Balance is: {total_balance}")
            deposit_again = input("Do You want to deposit again 'y' for 'yes' 'n' for 'no': ").lower()
            if deposit_again == "y":
                continue
            elif deposit_again == "n":
                choice_main_menu(user_name)
                break
            else:
                print("Invalid Option Try Again:")
        else:
            print("Please Enter a Valid Amount")
            choice_deposit()
            break


def choice_withdraw():
    print("Cash Withdraw")
    while True:
        global total_withdraw, total_balance
        current_withdraw = input("Enter Amount for Withdraw: ")
        if current_withdraw.isdigit():
            if int(current_withdraw) > total_balance:
                print(f"Insufficient Balance.\nYour Available Total Balance is {total_balance} in Your Account")
                continue
            total_balance -= int(current_withdraw)
            print(f"Please Collect Your Cash \nYour Available Balance is:{total_balance}")
            withdraw_again = input("Do you want to Withdraw again 'y' for 'yes' 'n' for 'no': ").lower()
            if withdraw_again == "y":
                continue
            elif withdraw_again == "n":
                choice_main_menu(user_name)
                break
            else:
                print("Invalid Selection")
                choice_withdraw()
                break
        else:
            print("Enter a Valid Amount")
            choice_withdraw()
            break


def choice_fast_cash():
    print("Fast Cash")
    while True:
        global total_withdraw, total_balance
        print("""
        1. 1000         2. 5000
        3. 2000         4. 10000
        5. 15000        6. 20000
        7. Other        8. Back""")
        current_withdraw = input("Choose Desired Option: ")
        if current_withdraw == "1":
            if total_balance < 1000:
                print(f"Insufficient Balance \nYour Current Total Balance is:Rs.{total_balance}/-")
            else:
                total_balance -= 1000
                print(f"Please Collect Your Cash \nYour Available Balance is:{total_balance}")
        elif current_withdraw == "2":
            if total_balance < 5000:
                print(f"Insufficient Balance \nYour Current Total Balance is:Rs.{total_balance}/-")
            else:
                total_balance -= 5000
                print(f"Please Collect Your Cash \nYour Available Balance is:{total_balance}")
        elif current_withdraw == "3":
            if total_balance < 2000:
                print(f"Insufficient Balance \nYour Current Total Balance is:Rs.{total_balance}/-")
            else:
                total_balance -= 2000
                print(f"Please Collect Your Cash \nYour Available Balance is:{total_balance}")
        elif current_withdraw == "4":
            if total_balance < 10000:
                print(f"Insufficient Balance \nYour Current Total Balance is:Rs.{total_balance}/-")
            else:
                total_balance -= 10000
                print(f"Please Collect Your Cash \nYour Available Balance is:{total_balance}")
        elif current_withdraw == "5":
            if total_balance < 15000:
                print(f"Insufficient Balance \nYour Current Total Balance is:Rs.{total_balance}/-")
            else:
                total_balance -= 15000
                print(f"Please Collect Your Cash \nYour Available Balance is:{total_balance}")
        elif current_withdraw == "6":
            if total_balance < 20000:
                print(f"Insufficient Balance \nYour Current Total Balance is:Rs.{total_balance}/-")
            else:
                total_balance -= 20000
                print(f"Please Collect Your Cash \nYour Available Balance is:{total_balance}")
        elif current_withdraw == "7":
            other_withdraw = input("Enter an Amount to Withdraw: ")
            if int(other_withdraw) > total_balance:
                print(f"Insufficient Balance!!! \nYour Available Balance is:{total_balance}")
                continue
            total_balance -= int(other_withdraw)
            print(f"Please Collect Your Cash \nYour Available Balance is:{total_balance}")
        elif current_withdraw == "8":
            choice_main_menu(user_name)
            break
        else:
            print("Invalid Selection Try Again:")
            choice_fast_cash()
            break
        withdraw_again = input("Do you want to Withdraw again 'y' for 'yes' 'n' for 'no': ").lower()
        if withdraw_again == "y":
            continue
        elif withdraw_again == "n":
            choice_main_menu(user_name)
            break
        else:
            print("Invalid Selection")
            # choice_fast_cash()


def choice_change_pin():
    print("Change Your Pin")
    global account_pin
    change_pin = input("Do you really want to change your PIN 'y' for 'yes' 'n' for 'no': ").lower()
    if change_pin == "y":
        new_pin = input("Enter New PIN: ")
        if new_pin.isdigit():
            reenter_new_pin = input("Re-enter Your New Pin Again: ")
            if reenter_new_pin == new_pin:
                print("You PIN Has Been Changed Successfully")
                account_pin = reenter_new_pin
                choice_1()
            else:
                print("Your PIN doesn't matched ")
                choice_change_pin()
        else:
            print("PIN must be a 4 digit Number")
            choice_change_pin()
    else:
        choice_main_menu(user_name)


def choice_pay_amount():
    print("Pay Amount")
    while True:
        global total_balance
        payee_name = input("Enter The Name of Payee: ")
        payee_amount = input("Enter The Amount To Pay: ")
        payee_remarks = input("Enter Your Remarks: ")
        if payee_amount.isdigit():
            if int(payee_amount) > total_balance:
                print(f"Insufficient Balance To Pay \nYour Total Balance is: {total_balance}")
                continue
            else:
                total_balance -= int(payee_amount)
                print(f"You have paid Rs. {payee_amount}/- to {payee_name} for {payee_remarks}")
                print(f"Your Remaining Balance is:Rs.{total_balance}/-")
                pay_more = input("Do you want to pay more 'y' for 'yes' 'n' for 'no': ").lower()
                if pay_more == "y":
                    choice_pay_amount()
                    break
                elif pay_more == "n":
                    choice_main_menu(user_name)
                    break
                else:
                    print("Invalid Selection Try Again: ")
                choice_main_menu(user_name)
                break
        else:
            print("Please Enter Valid Amount: ")


def choice_exit():
    print("See You Again!! Have a Great Time")
    exit()


def choice_1():
    pin_retries = 3
    global account_pin
    # account_pin = "4516"
    while pin_retries > 0:
        user_pin = input("Enter Your 4 digit Pin: ")
        if not user_pin.isdigit():
            print("Enter Valid Code in digits")
            continue
        if user_pin == account_pin:
            # print("Welcome To Your Account")
            choice_main_menu(user_name)
            break
        else:
            print("Wrong Pin Try Again:")
            pin_retries -= 1
            print(f"Re-Try Left: {pin_retries} ")
            if pin_retries == 0:
                print("Your Account has been blocked")







print("""Welcome To NIBL Bank
1. Insert Your Card
2. Exit""")
user_choice = input("Enter Your Choice: ")
if user_choice == "2":
    print("Thanks for using our services")
elif user_choice == "1":
    choice_1()
else:
    print("Wrong Input")
