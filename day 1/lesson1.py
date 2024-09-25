from turtle import *


#we want to pant a house

#step 1:  draw a square
speed(5)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawin a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawinh a window

color("brown")
begin_fill()
left(30)
forward(65)
left(90)
forward(65)
left(90)
forward(65)
end_fill()

color("red")
right(90)
forward(65)
color("brown")
begin_fill()
right(90)
forward(65)
left(90)
forward(65)
left(90)
forward(65)
end_fill()


exitonclick()
