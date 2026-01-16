import turtle   #importing library

turtle.Screen().bgcolor("light blue")

my_pen = turtle.Turtle()   #defined variable

#iterate loop for total number of sides
for i in range(4):
    my_pen.forward(100)
    my_pen.right(90)

turtle.done()
