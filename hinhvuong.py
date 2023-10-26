import turtle
t = turtle.Turtle()
t.hideturtle()

def square(a):
    for i in range(4):
        t.fd(a)
        t.right(90)
    turtle.done()
square(100)