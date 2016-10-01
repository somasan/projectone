import turtle
turtle.shape('turtle')

def circ(n, a):
    i = 0
    while i < 360:
         turtle.forward(a)
         turtle.left(1)
         i += 1
    while i > 0:
         turtle.forward(a)
         turtle.right(1)
         i -= 1
    if n != 0:
        circ(n-1, 1.1 * a)
    else:
        input()
turtle.left(90)
circ(2, 1)