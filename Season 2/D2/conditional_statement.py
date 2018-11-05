yob =int(input("When were you born? "))
t = 2018 - yob
print("Your age is", t)

if t<10:
    print("Baby.")
elif t<18:
    print("Teenager.")
else:
    print("Not baby.")