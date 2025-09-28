# from turtle import *

# lt(90)
# screensize(2000,2000)
# tracer(0)
# k=15
# for i in range(14):
#     for f in range(3):
#         fd(3*k)
#         rt(90)
#     lt(180)
# up()
# for x in range(-10,10):
#     for y in range(-10,10):
#         goto(x*k,y*k)
#         dot(4, 'purple')

# exitonclick()
# update()
from turtle import *

lt(90)
screensize(2000,2000)
tracer(0)
k=10
for i in range(4):
    fd(27*k)
    rt(90)
    fd(21*k)
    rt(90)
up()
fd(3*k)
rt(90)
fd(7*k)
lt(90)
down()
for i in range(4):
    fd(73*k)
    rt(90)
    fd(91*k)
    rt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(4, 'purple')

exitonclick()
