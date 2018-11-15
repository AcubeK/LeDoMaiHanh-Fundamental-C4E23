a = int(input("Enter number a = "))
x = input("Operator (+, -, x, /): ")
b = int(input("Enter number b = "))

print(a, x, b, "=", end =" ")

if x == "/":
    print(a/b)
    if b == 0:
        print("Can't divide by zero")
elif x == "x":
    print(a*b)
elif x == "+":
    print(a+b)
elif x == "-":
    print(a-b)
else:
    print("\n", "Command not valid.")
