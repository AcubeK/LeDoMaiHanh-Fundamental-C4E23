# use turtle to draw a square

from turtle import *

color("yellow")
begin_fill()

for i in range (4):
    forward(200)
    left(90)

end_fill()

mainloop()