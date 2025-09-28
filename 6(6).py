from turtle import *

lt(90)
screensize(2000,2000)
k=15
tracer(0)

for i in range(2):
    fd(21*k)
    rt(90)
    fd(27*k)
    rt(90)
up()
fd(9*k)
rt(90)
fd(10*k)
lt(90)
down()
for i in range(2):
    fd(86*k)
    rt(90)
    fd(47*k)
    rt(90)
up()
for x in range(-30,40):
    for y in range(-30,40):
        goto(x*k,y*k)
        dot(5, 'purple')
exitonclick()
