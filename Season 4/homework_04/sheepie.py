# shepherd exercise  

shpsz = [86, 66, 75, 92, 100, 47, 219]

print("Hiya, the name's H and these are my pals' sizes: ")
print(shpsz)
minshp = shpsz[0]
for i in len(shpsz):
    if minshp < shpsz[i]:
        minshp = shpsz[i]
