# use turtle to draw n circle from 1 point symmetrically

n = int(input("Please enter the number of circles (n>=1; integer): "))
deg = 360/n

from turtle import *
shape("turtle")
speed(0)

for i in range (n):
    circle(100)
    left(deg)

mainloop()
