# use turtle to draw a triangle

from turtle import *
shape("turtle")

color("yellow")
begin_fill()

for i in range (3):
    forward(200)
    left(120)

end_fill()

mainloop()