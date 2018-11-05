print()
print("Register.")
pw = input("Enter your password: ")
while   not pw.isalpha() and not pw.isdigit() and not pw.islower()\
        and not pw.isupper() and not len(pw)>8:

    print("Password is not valid.")
    
    if pw.isalpha():
        print("Must contains at least one number.")
    if pw.isdigit():
        print("Must contains at least one letter.")
    if pw.islower():
        print("Must contains at least one uppercase.")
    if pw.isupper():
        print("Must contains at least one lowercase.")
    if len(pw)<9:
        print("Must contains at least 9 characters.")
    
    pw = input("Enter your password: ")
else:
    print("Password is valid.")