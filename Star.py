import turtle

turtle.color('red','blue')
turtle.begin_fill()

for x in range(300,0,-5):
    turtle.fd(x)
    turtle.rt(144)
    
turtle.end_fill()
