import turtle


def star(n, a):
    bob = turtle.Turtle(shape="turtle")
    bob.right(180/n)
    bob.speed(2)
    bob.color('green', 'yellow')
    marlin = turtle.Turtle(shape="turtle")
    marlin.penup()
    marlin.speed(2)
    marlin.goto(150, 0)
    marlin.pendown()
    marlin.color('red', 'blue')
    while True:
        bob.forward(100)
        marlin.forward(100)
        bob.left(180 - 180/n)
        marlin.left(180 - 180 / a)
        if abs(marlin.pos()) < 150:
            break
    turtle.done()

star(5, 11)

input()
