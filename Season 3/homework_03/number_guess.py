# [OPTIONAL] Implement guess my number game

from random import randint

x = randint(1,101)
count = 0

print("Enter 0 to give up.")

while True:
    i = int(input("Guess my integer(1-100): "))

    if i == 0:
        print("What a shame. The correct number was", x)
        print("You gave up after", count, "tries.")
        break
    elif i<0 or i>100:
        print("Are you joking, mate? >:(")
    elif i < x :
        print("My number is smaller.")
        count += 1
    elif i < x :
        print("My number is bigger.")
        count += 1
    else:
        print("You won :0c")
        print("Guesses taken:", count+1)
        break
    
    print()

        

