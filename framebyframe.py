from turtle import *
from superturtle.animation import animate
from superturtle.movement import update_position, fly
from shapes import triangle

for frame in animate(frames=60, loop=True):
    fly(-200,0)

    if frame.index > 0 :
        triangle(100,'pink')

    if frame.index > frame.num_frames/3:
        update_position(150,0)
        triangle(100,'pink')

    if frame.index > 2*(frame.num_frames/3):
        update_position(150,0)
        triangle(100,'pink')

