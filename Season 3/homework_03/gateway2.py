# implement superuser login

print("This is a superuser gateway.")

usrnm = input("Please enter username: ")
while usrnm != "c4e":
    print("You're not a superuser.")
    print()
    usrnm = input("Please enter username: ")

else:
    pwd = input("Please enter your password: ")
    while pwd != "codethechange":
        print("Incorrect password.")
        print()
        pwd = input("Please enter your password: ")
    else:
        print("Welcome, c4e.")
