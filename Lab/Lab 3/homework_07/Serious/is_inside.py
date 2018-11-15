def is_inside(l_1, l_2):
    if len(l_2) == 2:
        if l_1[0] < l_2[0] and l_1[1] < l_2[1]:
            x = True
        else:
            x = False
    
    else:
        if l_2[0] < l_1[0] < l_2[0] + l_2 [2] and l_2[1] < l_1[1] < l_2[1] + l_2[3]:
            x = True
        else:
            x = False

    return x

#test

x1 = is_inside([100, 120], [140, 60,     ])
x2 = is_inside([200, 120], [140, 60, 100, 200])
if x1 == False and x2 == True:
    print("Correct-o.")
else:
    print("Wrong.")