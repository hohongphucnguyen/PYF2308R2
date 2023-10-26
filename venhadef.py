import turtle
t = turtle.Turtle()
t.hideturtle()
def square(a,b):
    t.hideturtle()
    for i in range(2):
        t.fd(a)
        t.left(90)
        t.fd(b)
        t.left(90)
   
square(100,150)
t.penup()
t.goto(100,0)
t.pendown()
square(100,150)
t.penup()
t.goto(0,150)
t.pendown()
square(100,150)
t.penup()
t.goto(100,150)
t.pendown()
square(100,150)

turtle.done()