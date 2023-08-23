import turtle

turtle.color('red','yellow')
turtle.begin_fill()

for x in range(200,0,-2):
    turtle.fd(x)
    turtle.rt(90)
    
turtle.end_fill()
