import mlab
from models.activities import Activities
from models.habbit import Habbit

mlab.connect()
while True:
    # act_or_hab = input("activity or habbit?")
    # if act_or_hab == "a":
        tit = input("title? ")
        st = int(input("strength? ") or "0")
        knl = int(input("knowledge? ") or "0")
        cre = int(input("creative? ") or "0")
        per = int(input("personality? ") or "0")
        soc = int(input("social? ") or "0")
        activity = Activities(tit=tit, st=st,knl=knl,cre=cre,per=per,soc=soc)
        activity.save()
        print("activity saved")
    # if act_or_hab == "h":
    #     tit = input("title? ")
    #     bnf = input("benefit? ")
    #     st = int(input("strength? "))
    #     knl = int(input("knowledge? "))
    #     cre = int(input("creative? "))
    #     per = int(input("personality? "))
    #     soc = int(input("social? "))    
    #     habbit = Habbit(tit=tit ,st=st ,knl=knl ,cre= cre,per=per ,soc=soc,bnf=bnf )
    #     habbit.save()
    #     print("habbit added")
