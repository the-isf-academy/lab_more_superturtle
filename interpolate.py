from turtle import *
from superturtle.animation import animate
from superturtle.movement import fly
from shapes import rectangle


for frame in animate(frames=60, loop=True):
    fly(-200,0)
    height2 = frame.interpolate(start=30, stop=90, mirror=True)
    width = 100 
    rectangle(width, height2, 'forest green')


    fly(0,0)
    height1 = frame.interpolate(start=80, stop=120, mirror=True)
    width = 100 
    rectangle(width, height1, 'forest green')
