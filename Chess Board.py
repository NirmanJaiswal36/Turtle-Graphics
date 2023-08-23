import turtle

turtle.penup()
turtle.goto(-200,200)
turtle.pendown()
turtle.speed(20)
color=['black','white']

for a in range(8):
    for x in range(8):
        turtle.begin_fill()
        for y in range(4):
            turtle.fd(50)
            turtle.rt(90)
        turtle.fillcolor(color[(a+x)%2])
        turtle.end_fill()
        turtle.fd(50)
    turtle.penup()    
    turtle.goto(-200,200-50*(a+1))        
    turtle.pendown() 

