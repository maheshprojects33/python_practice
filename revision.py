# user_details = {}
# while True:
#     print(user_details)
#     create_user = input("Create user account y/n/q: ")
#     if create_user == "y":
#         username = input("Input Username: ")
#         password = input("Input Password: ")
#
#         user_details[username] = password
#         print(user_details.keys())
#         print(user_details.values())
#
#         print(f"user '{username}' created successfully")
#         continue
#     elif create_user == "n":
#         print("Login Now \n")
#         input_username = input("Input Username: ")
#         input_password = input("Input Password: ")
#
#         if input_username in user_details.keys():
#             # print("keys:", user_details.keys())
#             # print("values:", user_details.values())
#             # print(user_details)
#             if input_password in user_details[input_username]:
#                 print("User logged in successfully")
#             else:
#                 print("Invalid Credientials")
#         else:
#             print("No account found")
#     else:
#         # print(user_details)
#         break

user_details = {}
while True:
    user_choice = input("Create user account y/n/q: ")
    if user_choice == "y":
        username = input("Input Username: ")
        if username in user_details:
            print("user already exists")
            user_exists = input("Do you like to change your username? y/n: ")
            if user_exists == "y":
                new_username = input("Input Username: ")
                user_details[new_username] = user_details.pop(username)
                print("New Username Updated")
                change_pwd = input("Do you like to change your password? y/n: ")

            else:
                change_pwd = input("Do you like to change your password? y/n: ")
                if change_pwd == "y":
                    while True:
                        old_password = input("Input your old password: ")
                        if old_password in user_details[username]:
                            new_password = input("Input New Password: ")
                            user_details[username] = new_password
                            print("New Password Updated")
                            break
                        else:
                            print("Old password not matched")
                else:
                    continue
        else:
            password = input("Input Password: ")

            user_details[username] = password
            print("User Created Successfully")

    elif user_choice == "n":
        print("!!! LogIn to your account !!! ")
        login_name = input("Input Username: ")


        if login_name in user_details.keys():
            print("user found")
            login_pass = input("Input Password: ")
            if login_pass in user_details[login_name]:
                print("User Logged in Successfully")
            else:
                print("Invalid password")
        else:
            print("User Not Found")


    elif user_choice == "q":
        break
    else:
        print("Invalid Input, Try Again.....")

    print(user_details)
