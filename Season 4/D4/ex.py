exp = ["decapitation", "laceration", "gutspill", "body horror", "meat soup"]


print("Here's a small dictionary")
print (*exp, sep = "    ")

exp = {
    "decapitation": "It's an act of beheading, usually with a sharp object or weapon.",
    "laceration": "It's a term for cuts and wounds.",
    "gutspill": "It's what it sounds like. A term for guts being spilled. A popular tag in the world of eroguro.",
    "body horror": "A not so unusual term for body modifications and transformation.",
    "meat soup": "Meat being grinded into tiny pieces like porridge.",
    "choking": "It's an act of preventing one from inhaling by squeezing one's throat."
}
print("Enter x to exit.")
while True:
    x = input("Your choice? ")

    if x == "x":
        break

    if x in exp:
        print(exp[x])
    else:
        print("Not found.")
        t = input("Do you want to contribute? (y/n) ")
        if t == "y":
            exp[x] = input("Please make your sacrifices: ")
            print(*exp, sep = "     ")
    
    k = input("Does the definition satify your personal need?(y/n): ")
    
    if k == "n":
        kk = input("Wasn't I enough to you?(y/n): ")
        if kk == "n":
            exp[x] = input("How can it be better? ")
            print(*exp, sep = "     ")
        else:
            print("Farewell.")
            del exp[x]
            print(*exp, sep = "     ")
    


