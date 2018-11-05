s = input("Enter a text: ")
if not s.isupper() and not s.islower() and not s.isdigit():
     print("Contains both lower and upper case.")
else:
    print("Does not contains both.")