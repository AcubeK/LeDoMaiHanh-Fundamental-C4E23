# scramble a randomly picked word from a word list and let user guesses

from random import *

words = ["hopeful", "despair", "malicious", "mastermind"]
chsnwrd = choice(words)
print("Enter x to give up.")

shfl = list(chsnwrd)
shuffle(shfl)
shfld = ' '.join(shfl)
print(shfld)

while True:
    x = input("Guess the unscrambled word: ")
    if x == chsnwrd:
        print("You got it, my pal.")
        break
    elif x == "x":
        print("Ahh, ok. The answer is:", chsnwrd)
        break
    else:
        print("Try again.")