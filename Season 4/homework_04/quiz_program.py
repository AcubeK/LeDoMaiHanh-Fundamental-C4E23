q1 = [35, 36, 40, 44]

print("Ring-a-ding-ding, it's quiz time, folks!! :D")
print("Question 1: If x = 8, then what is the value of 4(x+3)?")

for i, v in enumerate(q1):
    print(i+1, v, sep =". ")

y = int(input("Enter your choice: "))
if y == "4" or y == "44":
    print("You're correct!")
else:
    print("Congrats, you failed a basic human function. :C")