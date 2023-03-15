# def split_bill():
# Ask user for the number of friends
# num_friends = int(input("How many friends will split the bill? "))
#
# # Ask for the name of each friend
# friend_names = []
# for i in range(num_friends):
#     name = input(f"Enter the name of friend {i+1}: ")
#     friend_names.append(name)
# print(friend_names)
# # Ask for the bill amount for each friend
# friend_bills = {}
# for name in friend_names:
#     total_bill = 0
#     while True:
#         bill = float(input(f"Enter the bill amount for {name}: "))
#         total_bill += bill
#         more_bills = input(f"Does {name} have another bill to add? (y/n) ")
#         if more_bills.lower() == "n":
#             break
#     friend_bills[name] = total_bill
#     print(friend_bills)
#
# # Calculate individual total and split amount for each friend
# total_amount = sum(friend_bills.values())
# split_amount = total_amount / num_friends
# results = {}
# for name, total_bill in friend_bills.items():
#     individual_total = total_bill
#     split = total_bill - split_amount
#     results[name] = {"individual_total": individual_total, "split": split}
#
# # Print the results
# print("Results:")
# for name in friend_names:
#     print(f"{name}: {results[name]['individual_total']} (split: {results[name]['split']})")


# user = split_bill()

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



# #
# # while True:
# #
# #     if total_friends.isdigit():
# #         print("""
# #     1. Input All Your Bills
# #     2. Input Total Amount Only
# #     3. Exit / Quit
# #             """)
# #         break
# #     else:
# #         print("It Must Be Number")
# # def get_total_friends():
# #     while True:
# #         try:
# #             total_friends = int(input("How many friends are you to split the bill? "))
# #             return total_friends
# #         except ValueError:
# #             print("Total Friends Must be a Number")
#
#
# def ans_1():
#     print(f"""
# Total Friends           : {friends}
# Total of Individual     : {individual_totals}
# Total Bill Amount       : Rs.
# Individual Contribution : Rs.
# """)
#
#
# def ans_2():
#     print(f"""
# Total Friends           : {friends}
# Total Bill Amount       : Rs.{total_amount}
# Individual Contribution : Rs.{split:.2f}
# """)
#
#

#
# while True:
#     split_option = input("Choose an option for Calculation: ")
#     if split_option == "1":
#         friends = get_total_friends()
#         friends_name = []
#         individual_bill_amount = {}
#         results = {}
#         for names in range(friends):
#             name = input(f"Enter The Name of Friend {names + 1}: ")
#             friends_name.append(name)
#
        # for names in friends_name:
        #     individual_total = 0
        #     bill_count = 1
        #     print(f"--- Enter The Bill Amount of '{names}' ---")
#             while True:
#                 try:
#                     bill = float(input(f"Enter Total Amount of bill no.{bill_count}: "))
#                     individual_total += bill
#                     # print(individual_total)
#
#                 except ValueError:
#                     print("ERROR: ### 'Bill Amount Should Be A Number' ###")
#                     continue
#
                # while True:
                #     more_bill = input(f"Do You Have More Bill To Add '{names}' (y/n): ").lower()
                #     if more_bill == "y":
                #         bill_count += 1
                #         individual_bill_amount[names] = individual_total
                #         # print(individual_bill_amount)
                #         break
                #     elif more_bill == "n":
                #         individual_bill_amount[names] = individual_total
                #         # print(individual_bill_amount)
                #         break
                #     else:
                #         print("Invalid Option Type Either 'y' for 'yes' or 'n' for 'no'")
                #         continue
#
#                 # print(individual_bill_amount)
#                 # print(individual_bill_amount.values())
#                 # print(individual_bill_amount.items())
#                 # print(individual_bill_amount.keys())
#                 total_bill = sum(individual_bill_amount.values())
#                 # print(total_bill)
#
#                 split_amount = total_bill / friends
#
#
#                 for key, value in individual_bill_amount.items():
#                     individual_totals = value
#                     # print(individual_totals, "INDV_TOT")
#                     # print(total_bill)
#                     # print(split_amount)
#                     split_individual = individual_totals - split_amount
#                     results[key] = {"individual_totals": individual_totals, "split": split_individual}
#                 # print(results)
#                 # print(friends_name)
#                 # print(friends)
#                 for namex in friends_name:
#                     print(f"""
#                     Total Friends                 = {friends}
#                     Total Bill Amount of {namex}  = {results[namex]['individual_totals']}
#                     Total No. of Bills of {namex} =
#                     Total Amount to Split         = {split_amount}
#                     Total Amount to Contribute    =
#                     """)
#
#
#                 # Print the results
#                 #     print("Results:")
#                 #     for name in friend_names:
#                 #         print(f"{name}: {results[name]['individual_total']} (split: {results[name]['split']})")
#
#
#
#
#
#                 if more_bill == "n":
#                     break
#
#
#
#
#
#
#     elif split_option == "2":
#         while True:
#             friends = get_total_friends()
#             while True:
#                 total_amount = input("Enter Your Total Bill Amount For Split: ")
#                 try:
#                     split = float(total_amount) / float(friends)
#                     ans_2()
#                     quit()
#                 except ValueError:
#                     print("Total Bill Must Be a Valid Number")
#             # else:
#             #     print("Total Friends Must be a Number")
#     elif split_option == "3":
#         print("Thanks For Using Our Split Bill Application")
#         quit()
#     else:
#         print("Invalid Option Please Enter Either 1, 2 or 3: ")
