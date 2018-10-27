# scramble a specific word and let user guesses

from random import *

print("Enter x to give up.")
chsnwrd = "salvation"
b = list(chsnwrd)                        #break down the words into list
shuffle(b)
c = ' '.join(b)                          #join the shuffled words into one
print(c)                                 #can't jam straight in?

while True:
    x = input("Guess the unscrambled word: ")
    if x == chsnwrd:
        print("Ah-ha, correct!")
        break
    elif x == "x":
        print("Aw, the correct word was:", chsnwrd)
        break
    else:
        print("Try again.")