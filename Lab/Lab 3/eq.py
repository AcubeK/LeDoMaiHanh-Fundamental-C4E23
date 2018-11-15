from random import *
from function_intro import eval

def generate_quiz():
    a = randint(0, 20)
    b = randint(0, 20)
    x = choice(["+", "-", "x", "/"])
    s = eval(a, b, x)

    return a, b, x, s

a, b, x, s = generate_quiz()
error = randint(-2, 2)
d = choice([s, s + error])


print("Division will be rounded. (Below 5 -> down, From 5 and above -> up)")
print(a, x, b, "=", d)

ans = input("(Y/N)? ").lower()

if (d == s and ans == "y") or ( d != s and ans == "n" ):
    print("Correct.")
else:
    print("False.")




