#3 задание из КЕГЭ - черепаха
from turtle import *
lt(90)
screensize(2000,2000)
k=30
for i in range(16):
    lt(36)
    fd(4*k)
    lt(36)
up()
for x in range(-10,10):
    for y in range(-10,10):
        goto(x*k,y*k)
        dot(4, 'purple')

exitonclick(0)
update()