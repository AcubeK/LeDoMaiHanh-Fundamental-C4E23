prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15

}

total = 0
    
for x in stock:
    print((x).upper())
    print("Price:", prices[x])
    print("Stock:", stock[x])
    print()
    
    total += stock[x]*prices[x]

print("If you sold all of them, you'd get:", total)

