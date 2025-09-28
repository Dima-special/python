from turtle import *

rt(90)
screensize(2000,2000)
tracer(0)
k=15
for i in range(8):
    rt(45)
    fd(11*k)
    rt(45)
up()
for x in range(-15,15):
    for y in range(-15,15):
        goto(x*k,y*k)
        dot(2, "purple")
exitonclick()
update()