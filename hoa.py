import turtle
t = turtle.Turtle()
def ellipse(r):
    for x in range(2):
        for i in range(0,2):
            t.circle(r,90)
            r /= 2
        r *= 4
while True:
    ellipse(100)
    t.right(20)

        

