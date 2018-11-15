from random import *

def eval(a, b, x):
    if x == "/":
        if b == 0:
            print("Can't divide by zero.")
            s = "Null."
        else:
            s = a / b
       
    elif x == "x":
        s = a * b
    elif x == "+":
        s = a + b
    elif x == "-":
        s = a - b

    return s

def generate_quiz():
    a = randint(0, 20)
    b = randint(0, 20)
    x = choice(["+", "-", "x", "/"])
    error = randint(-2, 2)
    s = choice([eval(a, b, x), eval(a, b, x) + error])


    return a, b, x, s

a, b, x, s = generate_quiz()

def check_answer(a, b, x, s, user_choice):
    if (s == eval(a, b, x) and user_choice == True) or (s != eval(a, b, x) and user_choice == False):
        return True
    else:
        return False
