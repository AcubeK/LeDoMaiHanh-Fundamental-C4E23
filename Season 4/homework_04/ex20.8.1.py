# program which read input string and print the occurence of each letter in alphabetic orders


string = input("Please enter your string: ").lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"

count = {} 
for x in string:
    if x in alphabet: 
        if x in count:
            count[x] +=1
        else:
            count[x] = 1

for x in alphabet:
    if x in count:
        print(x, count[x], sep = ": ")
    else:
        pass