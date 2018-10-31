# shephard exercise

shpsz = [86, 66, 75, 92, 100, 47, 219]
print("Hiya, the name's H and these are my pals' sizes: ", shpsz, sep ="\n")
print()

maxsz = shpsz[0]
n = int(input("For how many months do you want to keep shearing before traveling? (integer) "))
for x in range(n):
        print("MONTH", x+1)

        
        for i in range(len(shpsz)):
                shpsz[i] += 50
        print("A month passed. The pals' sizes increased:", shpsz, sep = "\n")  

        for i in range(len(shpsz)):
                if maxsz < shpsz[i]:
                        maxsz = shpsz[i]
        k = shpsz.index(maxsz)
        shpsz[k] = 8
        print("The unfortunate one with the size of", maxsz, "will be sheared.")
        print("Here's the flock after shearing: ", shpsz, sep ="\n")
    
        print()

        maxsz = 0

print("Alright, you got this, H. Traveling the world is not something to be taken lightly.")
print("Let's see how much I would get selling my pals.")
sumsz = 0
for i in range(len(shpsz)):
        sumsz += shpsz[i]
money = sumsz * 2
print("The size of my flock in total: ", sumsz)
print("And I'd get:", sumsz, "*", "2$ =", money)



        

