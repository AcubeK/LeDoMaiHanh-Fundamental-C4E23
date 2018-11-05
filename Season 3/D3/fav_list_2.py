items = ["rhythm game", "horror tags", "pixelated things"]

print("Here your things: ", *items, sep = "\n")

i = int(input("Position u wanna update? "))
r= input("What's the new deal? ")

items[i-1] = r
print(*items, sep="\n")