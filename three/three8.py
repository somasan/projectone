import turtle
turtle.shape('turtle')
i = 10
while i < 100:
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i+10)
    turtle.left(90)
    turtle.forward(i+10)
    turtle.left(90)
    i = i + 20
input()