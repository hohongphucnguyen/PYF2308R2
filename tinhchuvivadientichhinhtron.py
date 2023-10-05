import turtle
import math
ban_kinh = int(input(' nhập bán kính hình tròn '))
t = turtle.Turtle()
t.hideturtle()
t.pensize(1)
t.color('red')
t.circle(ban_kinh)
turtle.done
chu_vi = 2 * math.pi * ban_kinh
dien_tich = math.pi * (ban_kinh**2)
print(f' chu vi cua hinh tron la {chu_vi}')
print(f' dien tich cua hinh tron là {dien_tich}')
