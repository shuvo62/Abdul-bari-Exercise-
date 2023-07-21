Password = input("Enter password: ")
Con_password = input("Confirm password: ")
if Password == Con_password:
    print("Correct Password")
else:
    if Password.casefold() == Con_password.casefold():
        print("Check if the cases are correct")
    else:
        print("Incorrect Password")
