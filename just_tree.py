from turtle import *
from superturtle.animation import *
from superturtle.movement import *
from superturtle.easing import easeOutSine, easeInSine, easeOutExpo, easeInExpo
from shapes import *
from tree_parts import *

colormode(255)


for frame in animate(frames=120, loop=True):
    with frame.translate(start=[-300, 200], stop=[300, 200]):
        filled_circle(30,"white")



    red = frame.interpolate(start=170, stop=250, mirror=True)
    height = frame.interpolate(start=30, stop=90, mirror=True)
    branch_size = 60
    tree_trunk(30,height)
    update_position(15,height+branch_size/2)
    tree_top(branch_size)

    bgcolor(int(red//1),180,250)

