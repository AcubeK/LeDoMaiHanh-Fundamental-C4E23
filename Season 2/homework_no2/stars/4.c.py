# print out 9 (stars and xs) in total

for i in range(1, 10):
    if i%2 == 1:
        print("* ", end="")
    else:
        print("x ", end="")