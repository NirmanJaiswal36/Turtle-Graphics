import turtle
from random import *
turtle.shape('turtle')
mylist=[]
colorlist=['purple','blue','green','orange']
for ch in range(4):
    ch=turtle.clone()
    mylist.append(ch)
    
for x in range(4):
    mylist[x].color(colorlist[x])
    mylist[x].penup()
    mylist[x].goto(-200,200-40*x)
    mylist[x].pendown()

turtle.penup()
turtle.goto(-180,220)
turtle.pendown()
turtle.speed(50)

for y in range(1,16):
    turtle.write(y)
    turtle.rt(90)
    turtle.fd(200)
    turtle.lt(90)
    turtle.penup()
    turtle.goto(-180+20*y,220)
    turtle.pendown()
turtle.hideturtle()


for z in range(550):
    mylist[randint(0,3)].fd(2)
    
