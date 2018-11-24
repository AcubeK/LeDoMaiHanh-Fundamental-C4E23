import mlab
from fetch_convert_save import Q_A_sheet
from random import randint, choice
import html

mlab.connect()
sheet = Q_A_sheet.objects()

counter = 0
point = 0

while True:
    ans_list = []
    i = randint(0, len(sheet))

    print(sheet[i].question)
    if type(sheet[i].correct_ans) == str:
        ans_list = list(sheet[i].incorrect_ans)
        ans_list.append(sheet[i].correct_ans)
    else:
        ans_list = [True, False]
    
    print(ans_list)
    n = 0
    while n < len(ans_list):
        n += 1
        x = ""
        while x == "":
            x = choice(ans_list)
        ans_list[ans_list.index(x)] = ""
        if x == sheet[i].correct_ans:
            k = n
        if type(x) == str:
            x = html.unescape(x)
        print(n, x, sep = ". " )
    
    ans = input("Please enter your answer (from 1 to 4)(press c to exit): ")

    if ans.lower() == "c":
        print("You've answered correctly", point, "out of", counter)
        break
    elif int(ans) == k:
        print("Correct.", "\n")
        point += 1
    else: 
        print("D:", "\n")

    counter += 1

        
