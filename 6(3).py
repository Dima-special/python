from turtle import *

lt(90)
screensize(2000,2000)
k=15
tracer(0)
fd(9*k)
rt(90)
for i in range(2):
    fd(3*k)
    rt(90)
    fd(3*k)
    rt(270)
for t in range(2):
    fd(3*k)
    rt(90)
fd(9*k)
up()
for x in range(-10,10):
    for y in range(-10,10):
        goto(x*k,y*k)
        dot(4, 'purple')

exitonclick()
update()
