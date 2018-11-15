from random import *

a = randint(0, 20)
b = randint(0, 20)
error = randint(-2, 2)


x = choice(["+", "-", "x", "/"])

if x == "/":
    tru = round(a/b)
elif x == "x":
    tru =a*b
elif x == "+":
    tru = a+b
else:
    tru = a-b

d = choice([tru, tru+error])

print("Division will be rounded. (Below 5 -> down, From 5 and above -> up)")
print(a, x, b, "=", d)

ans = input("(Y/N)? ").lower()

if (d == tru and ans == "y") or ( d != tru and ans == "n" ):
    print("Correct.")
else:
    print("False.")




