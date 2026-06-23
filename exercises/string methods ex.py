# user input
# username not more than 15 characters long
# no spaces
# no digits



username = input("Enter your username: ")

if len(username) > 15:
    print("username can't be more than 12 characters long")
elif not username.find(" ") == -1:
    print("Your username can't contain space")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"welcome {username}")