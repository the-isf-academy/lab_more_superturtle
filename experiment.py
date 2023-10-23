# this code has been adapted from the offical superturtle documentation
# https://superturtle.readthedocs.io/en/latest/introduction.html

from turtle import *
from superturtle.animation import *
from superturtle.movement import *
from shapes import *
from random import randint

colormode(255)

rectangle_size = 60
triangle_size = 30

for frame in animate(60, loop=True):
    with frame.rotate(0, 360):
        penup()
        forward(100)
        pendown()
        rectangle(rectangle_size,rectangle_size, 'dark sea green')


        with frame.rotate(0, 360, cycles=2):
            penup()
            forward(100)
            pendown()
            triangle(triangle_size,'coral')

        with frame.rotate(0, 360, cycles=1):
            penup()
            forward(100)
            right(45)
            pendown()
            triangle(triangle_size,'coral')


