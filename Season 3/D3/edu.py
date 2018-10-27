#item1 = "Poison"
#item2 = "Glass Shards"
#item3 = "Hand"
#item4 = "Eyes"
#item5 = "Nail Polish"

# items = []
# print(items)
# print(type(items))

items = ["Poison", "Glass Shards"]
print(items)
items.append("Hand")
print(*items, sep=", ")