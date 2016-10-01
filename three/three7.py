import turtle
turtle.shape('turtle')
a = 1
i = 1
while a < 10000:
    turtle.forward(a*i/360)
    turtle.left(i)
    a += 1
input()