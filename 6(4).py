from turtle import *

lt(90)
screensize(2000,2000)
k=15
tracer(0)
for i in range(5):
    fd(15*k)
    lt(90)
    fd(25*k)
    lt(90)
up()
fd(4*k)
lt(90)
fd(12*k)
lt(90)
down()
for t in range(6):
    fd(38*k)
    rt(90)
    fd(22*k)
    rt(90)
up()
for x in range(-25,10):
    for y in range(-10,20):
        goto(x*k,y*k)
        dot(4, 'purple')

exitonclick()
update()
