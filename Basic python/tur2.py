import turtle
turtle.shape("turtle")
turtle.speed(0)
for side_len in range(20,200,1):
    for i in range(4):
        turtle.forward(side_len)
        turtle.left(90)

for side_len in range(20,200,3):
    for i in range(4):
        turtle.color("red")
        turtle.forward(side_len)
        turtle.right(90)

for side_len in range(20,200,10):
    for i in range(4):
        turtle.color("blue")
        turtle.backward(side_len)
        turtle.left(90)

for side_len in range(20,200,3):
    for i in range(4):
        turtle.color("green")
        turtle.backward(side_len)
        turtle.right(90)
turtle.exitonclick()
