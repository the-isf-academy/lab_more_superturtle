from turtle import *
from superturtle.animation import animate
from superturtle.movement import fly
from shapes import triangle


for frame in animate(frames=40, loop=False):
    with frame.rotate(start=0, stop=180):
        fly(-200,0)
        triangle(100,'blue')

    with frame.rotate(start=0, stop=180):
        fly(200,0)
        triangle(100,'red')

