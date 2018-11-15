def add(a, b):
    s = a + b
    return s


#call function


# 1 equation
# evaluate
# receive a, b, op
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

# s = eval(5, 0, "/")
# print(s)
    

# calculate ans and return
# use it