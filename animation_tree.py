from turtle import *
from superturtle.animation import *
from superturtle.movement import *
from shapes import *
from tree_parts import *

# change turtle color mode to rgb
colormode(255)


for frame in animate(frames=120, loop=True):
    # animate tree growth 
    height = frame.interpolate(start=30, stop=90, mirror=True)
    branch_size = 100
    
    tree_trunk(branch_size/3,height)
    update_position(20,height+(branch_size*.75))
    tree_top(branch_size)

    # change background color 
    red_bgval = int(frame.interpolate(start=170, stop=250, mirror=True))
    bgcolor(red_bgval, 180, 250)



    
