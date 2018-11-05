q1 = ["If x = 8, then what is the value of 4(x+3)?", 35, 36, 40, 44]
q2 = ["Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is his approximate average score?", 55, 65, 75, 85]

count =0

print("Ring-a-ding-ding, it's quiz time, folks!! :D")
print("Question 1:", q1[0])

for i in range(1, 5):
    print(i, q1[i], sep =". ")

y = int(input("Enter your choice: "))
if y == 4 or y == 44:
    print("You're correct!")
    count += 1
else:
    print("Congrats, you failed a basic human function. :C")

print("Question 2:", q2[0])

for i in range(1, 5):
    print(i, q2[i], sep =". ")

n = int(input("Enter your choice: "))
if n == 2 or n == 65:
    print("You're correct!")
    count += 1
else:
    print("Congrats, you failed a basic human function. :C")

print("You've answered correctly", count, "out of 2.")