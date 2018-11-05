
from turtle import *

for i in range(3, 7):

    if i%2==0:
        color('red')
    else:
        color('blue')
    
    for x in range(i):
        forward(150)
        left(360/i)

mainloop()