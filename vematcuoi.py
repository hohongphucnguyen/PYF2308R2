import turtle
t= turtle.Turtle()
turtle.bgcolor('light blue')
# vẽ hình chữ nhật
t.color('blue')
t.penup()
t.goto(-100,-100)
t.pendown()
t.begin_fill()
t.left(90)
t.forward(200)
t.right(90)
t.forward(150)
t.right(90)
t.forward(200)
t.right(90)
t.fd(150)
t.end_fill()
# vẽ cánh cửa
t.goto(-40,-100)
t.color('light green')
t.begin_fill()
t.right(90)
t.forward(80)
t.right(90)
t.forward(50)
t.right(90)
t.forward(80)
t.goto(-40,-100)
t.end_fill()
# vẽ tam giác
t.color("pink")
t.penup()
t.goto(-100,100)
t.pendown()
t.goto(-25,150)

