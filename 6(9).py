from turtle import *

speed(50)
up()
goto(0,0)
down()
lt(90)
k=15
tracer(0)

rt(315)
for i in range(7):
    fd(16*k)
    rt(45)
    fd(8*k)
    rt(135)
up()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(2, 'red')

