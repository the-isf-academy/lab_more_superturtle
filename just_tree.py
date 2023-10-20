from turtle import *
from superturtle.animation import animate
from superturtle.movement import *
from shapes import rectangle
from tree_parts import *


for frame in animate(frames=60, loop=True):
    height = frame.interpolate(start=30, stop=90, mirror=False)
    branch_size = 60
    tree_trunk(30,height)
    update_position(15,height+branch_size/2)
    tree_top(branch_size)
