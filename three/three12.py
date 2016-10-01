import turtle
turtle.shape('turtle')

def dug(n, a):
    i = 0
    while i < 180:
        turtle.forward(a)
        turtle.right(1)
        i += 1
    while i > 0:
        turtle.forward(0.1 * a)
        turtle.right(1)
        i -= 1
    if n != 0:
        dug(n - 1, a)
    else:
        input()
turtle.left(90)
dug(3, 1)