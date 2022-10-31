import turtle
import random

def square(height, length, space):
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(180)
    turtle.forward(length + space)


height = 27
length = 9
space = 6

for i in range(20):
    square(height, length, space)

    height = height + 10 * random.random()

turtle.exitonclick()
