import turtle

turtle.color('red','blue')
turtle.begin_fill()

for x in range(100,0,-1):
    turtle.fd(x)
    turtle.rt(45)
    
turtle.end_fill()
