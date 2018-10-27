# implement superuser login

print("This is a superuser gateway.")

usrnm = input("Please enter username: ")
if usrnm != "c4e" :
    print("You're not a superuser.")
else:
    pwd = input("Please enter your password: ")
    if pwd != "codethechange":
        print("Incorrect password.")
    else:
        print("Welcome, c4e.")
    