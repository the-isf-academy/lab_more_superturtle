from turtle import *
from superturtle.animation import animate
from superturtle.movement import fly
from shapes import triangle



for frame in animate(60, loop=True):
    with frame.scale(start=1, stop=2, first_frame=20):
        fly(-200,200)
        triangle(100,'coral')

    with frame.scale(start=2, stop=1, first_frame=40):
        fly(100,-100)
        triangle(100,'coral')


