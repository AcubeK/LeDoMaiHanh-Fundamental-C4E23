yob_str = input("Enter ur birthyear: ")
while not yob_str.isdigit():
    print("Error.")
    yob_str = input("Enter ur birthyear: ")
yob = int(yob_str)
age = 2018 - yob
print("Ur age is", age)