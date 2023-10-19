import turtle
t = turtle.Turtle()
d = int(input(' nhập khoảng cách từ tâm tới điểm cuối cùng mà bạn mong muốn '))
r = 5
while True:
    t.circle(r,180)
    r += 5
    if r ==d :
        break
    