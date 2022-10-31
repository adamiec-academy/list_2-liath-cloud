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
  
height = 90
length = 30
space = 20

for i in range(20):
  
  square(height, length, space)
  
  height = height + random.random()
