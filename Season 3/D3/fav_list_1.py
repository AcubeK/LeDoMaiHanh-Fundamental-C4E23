items = ["rhythm game", "horror tags", "trippy things"]
print("Here's a list of your weird stuffs, man: ", items)

i = input("Anything u wanna add? ")

while i != "no more":
    items.append(i)
    print(items)
    i = input("Anything u wanna add? ")