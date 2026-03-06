import turtle
turtle.shape("turtle")
turtle.color("blue")
counter=0
while counter<50: 
    for i in range(1, 4):
        for i in range(1,10):
            turtle.speed(0)
            turtle.forward(100)
            turtle.right(90)
        turtle.right(5)
       
    turtle.right(10)
    counter+=1
turtle.exitonclick()
