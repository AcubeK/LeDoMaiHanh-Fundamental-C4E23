# use turtle to draw 6 circle from 1 point symmetrically

from turtle import *
shape("turtle")
speed(0)

for i in range (6):
    circle(100)
    left(60)

mainloop()
