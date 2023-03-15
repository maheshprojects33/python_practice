def welcome():
    print("##### Welcome To Bill Splitter App #####")
    print("""
    1. Input All Your Bills (Option To Enter All Bills of Individuals)
    2. Input Total Amount Only (Grand Total Amount of All Your Expenses)
    3. Exit / Quit
    """)


def get_total_friends():
    while True:
        try:
            total_friends = int(input("How many friends are you to split the bill? "))
            return total_friends
        except ValueError:
            print("Total Friends Must be a Number")


def ans_2():
    print(f"""
Total Friends           : {friends}
Total Bill Amount       : Rs.{total_amount}
Individual Contribution : Rs.{split:.2f}
""")


def ans_1():
    for namex in friends_name:
        print(f"""
Total Friends = {friends}
Total Bill Amount of {namex} = {results[namex]['individual_totals']}
Total No. of Bills of {namex} = {results[namex]['bill']}
Total Amount to Split = {split_amount:.2f}
Total Amount to Contribute = {results[namex]['split']:.2f}
""")
    print("NOTE: The Person with '-' NEGATIVE AMOUNT needs to pay to other Friends with '+' POSITIVE AMOUNT ")


while True:
    welcome()
    split_option = input("Choose an option for Calculation: ")
    if split_option == "1":
        friends = get_total_friends()
        friends_name = []
        individual_bill_amount = {}
        individual_bill_number = {}
        results = {}
        for names in range(friends):
            name = input(f"Enter The Name of Friend {names + 1}: ")
            friends_name.append(name)

        for names in friends_name:
            individual_total = 0
            total_bill = 0
            bill_count = 1
            individual_bill_number[names] = 0
            print(f"--- Enter The Bill Amount of '{names}' ---")
            while True:
                try:
                    bill = float(input(f"Enter Total Amount of bill no.{bill_count}: "))
                    individual_total += bill
                    while True:
                        more_bill = input(f"Do You Have More Bill To Add '{names}' (y/n): ").lower()
                        if more_bill == "y":
                            bill_count += 1
                            individual_bill_amount[names] = individual_total
                            individual_bill_number[names] += 1
                            break
                        elif more_bill == "n":
                            individual_bill_amount[names] = individual_total
                            individual_bill_number[names] = bill_count
                            break
                        else:
                            print("Invalid Option Type Either 'y' for 'yes' or 'n' for 'no'")
                            continue
                    if more_bill == "n":
                        break
                except ValueError:
                    print("ERROR: ### 'Bill Amount Should Be A Number' ###")
                    continue

        total_bill = sum(individual_bill_amount.values())
        split_amount = total_bill / friends

        for key, value in individual_bill_amount.items():
            individual_totals = value
            split_individual = individual_totals - split_amount

            results[key] = {"individual_totals": individual_totals, "split": split_individual,
                            "bill": individual_bill_number[key]}

        ans_1()
        input("Press Enter To Continue...")

    elif split_option == "2":
        # Get Total Friends Prompt from get_total_friends method
        friends = get_total_friends()
        total_amount = float(input("Enter Your Total Bill Amount For Split: "))
        try:
            split = float(total_amount) / float(friends)
            ans_2()
            input("Press Enter To Continue...")
            continue
        except ValueError:
            print("Total Bill Must Be a Valid Number")

    elif split_option == "3":
        print("Thanks For Using Our Split Bill Application")
        quit()
    else:
        print("Invalid Option Please Enter Either 1, 2 or 3: ")
        continue

