import turtle
turtle.shape('turtle')
a = int(input())
i = 360/a
n = 0
while n < a:
    turtle.forward(100)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(100)
    n += 1
    turtle.left(180 + i)
input()