#Исполнитель чертежник
from turtle import *

lt(90)
screensize(2000,2000)
k=20
tracer(0)

for _ in range(-15,20):
    goto(xcor()+5*k, ycor()+4*k)
    goto(xcor()+4*k, ycor()-4*k)
    goto(xcor()-7*k, ycor()-2*k)
    goto(xcor()-2*k, ycor()+2*k)

up()
for x in range(-30,40):
    for y in range(-30,40):
        goto(x*k,y*k)
        dot(5, 'purple')
exitonclick()
