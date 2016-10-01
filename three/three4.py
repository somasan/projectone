import turtle
turtle.shape('turtle')
i = 0
turtle.begin_fill()
while i < 360:
    turtle.forward(1)
    turtle.left(1)
    i += 1
turtle.end_fill()
input()