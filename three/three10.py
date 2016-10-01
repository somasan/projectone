import turtle
turtle.shape('turtle')

def circ(n):
    i = 0
    while i < 360:
         turtle.forward(1)
         turtle.left(1)
         i += 1
    while i > 0:
         turtle.forward(1)
         turtle.right(1)
         i -= 1
    turtle.left(60)
    if n != 0:
        circ(n-1)
    else:
        input()
circ(2)
