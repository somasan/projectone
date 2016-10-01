import turtle
import math
turtle.shape('turtle')


def oct(n, R):
    turtle.begin_fill()
    turtle.left(90 - (360/(2*n)))
    for i in range(n):
        turtle.left(360/n)
        turtle.forward(R * 2 * math.sin(math.pi/n))
    turtle.end_fill()
    turtle.right(90 - (360 / (2 * n)))
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()

    if n == 10:
        input()
    else:
        oct(n+1, R+15)
oct(3, 30)
