import turtle
turtle.shape('turtle')

def circ(a):
    turtle.begin_fill()
    i = 0
    while i < 360:
         turtle.forward(a)
         turtle.left(1)
         i += 1
    turtle.end_fill()
def dug(a):
    i = 0
    while i < 180:
        turtle.forward(a)
        turtle.right(1)
        i += 1
turtle.color('black', 'yellow')
circ(1)
turtle.penup()
turtle.goto(30, 60)
turtle.pendown()
turtle.color('black', 'blue')
circ(0.1)
turtle.penup()
turtle.goto(-30, 60)
turtle.pendown()
turtle.color('black', 'blue')
circ(0.1)
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.pensize(10)
turtle.right(90)
turtle.forward(10)
turtle.penup()
turtle.goto(29, 40)
turtle.pendown()
turtle.color('red', 'yellow')
dug(0.5)
input()