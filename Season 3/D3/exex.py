print()
print("Register.")
pw = input("Enter your password: ")
while  True:

    print("Password is not valid.")
    
    if pw.isalpha():
        print("Must contains at least one number.")
    elif pw.isdigit():
        print("Must contains at least one letter.")
    elif pw.islower():
        print("Must contains at least one uppercase.")
    elif pw.isupper():
        print("Must contains at least one lowercase.")
    elif len(pw)<9:
        print("Must contains at least 9 characters.")
    else:
        break
    pw = input("Enter your password: ")
