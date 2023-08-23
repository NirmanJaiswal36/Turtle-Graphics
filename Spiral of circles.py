from turtle import*
speed(100)
def circles(num):
    circle(num)
myList=['black','green','blue','red']    
for z in range(4):
    color(myList[z])
    for y in range(10):
        for x in range(10):
            circle(150-6*x)
        rt(36)
    rt(18)    
        
        

