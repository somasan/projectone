import turtle
turtle.shape('turtle')
for i in range(10, 201, 20):
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.penup()
    turtle.right(45)
    turtle.forward((2*10**2)**0.5)
    turtle.left(135)
    turtle.pendown()
input()