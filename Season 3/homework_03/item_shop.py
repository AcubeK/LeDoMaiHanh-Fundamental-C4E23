#item shop

clth = ["T-shirt", "Sweater"]

while True:
    x = (input("Welcome to our shop. What do you want? (C, R, U, D) "))

    if x.upper() == "C":
        clth.append(input("What item you want to add? "))
    elif x.upper() == "U":
        i = int(input("Which position you want to update? "))
        clth[i-1] = input("New item? ")
    elif x.upper() == "D":
        u = int(input("What position do you want to delete? "))
        clth.pop(u-1)
    elif x.upper() == "R":
        pass
    else: 
        print("Command not available. Try again.")

    print("Our items: ", end="")
    print(*clth, sep = ", " )
    print()
