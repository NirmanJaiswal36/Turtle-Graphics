import turtle
mylist=['blue','black', 'red', 'yellow','green']
turtle.pensize(5)


for x in range(3):
    turtle.color(mylist[x])
    turtle.circle(100)
    turtle.penup()
    turtle.fd(225)
    turtle.pendown()

turtle.penup()
turtle.goto(112.5,-125)

for x in range(2):
    turtle.color(mylist[x+3])
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()
    turtle.fd(225)
    
    
    
