from turtle import *
from superturtle.animation import animate
from superturtle.easing import easeOutSine, easeInSine, easeOutExpo, easeInExpo
from shapes import triangle


for frame in animate(frames=100, loop=True):
    with frame.translate(start=[-200, 0], stop=[200, 0],easing=easeInExpo):
        triangle(100,'pink')

