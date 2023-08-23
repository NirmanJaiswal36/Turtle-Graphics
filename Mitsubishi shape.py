import turtle

turtle.color('red','blue')
turtle.begin_fill()

for y in range(8):
    for x in range(2):
        turtle.fd(100)
        turtle.rt(60)
        turtle.fd(100)
        turtle.rt(120)
    turtle.rt(45)
    
turtle.end_fill()
