items = ["rhythm game", "horror tags", "pixelated things"]

print("Here your things: ", *items, sep = "\n")

i = int(input("Anything u wanna cross off? "))
items.pop(i-1)

print(*items, sep ="\n")