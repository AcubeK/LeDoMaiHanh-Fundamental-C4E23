# print out n stars and xs in total (n is entered by users)

n = int(input("Please enter the numbers of stars and xs in total: "))
for i in range(1, n+1):
    if i%2 == 1:
        print("* ", end="")
    else:
        print("x ", end="")