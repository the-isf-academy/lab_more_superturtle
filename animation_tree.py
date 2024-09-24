from turtle import *
from superturtle.animation import animate
from superturtle.movement import fly
from shapes import *
from tree_parts import *
from random import randint
import settings

# change turtle color mode to rgb
colormode(255)


for frame in animate(frames=settings.TOTAL_FRAMES, loop=True):
    # animate tree growth 
    tree_height = frame.interpolate(start=30, stop=60, mirror=True)
    tree_width = 50

    
    # draws the tree 
    tree_full(tree_width, tree_height, settings.TREE_TRUNK_COLOR, settings.TREE_TOP_COLOR)


    # change background color 
    red_bgval = int(frame.interpolate(start=170, stop=250, mirror=True))
    bgcolor(red_bgval, 180, 250)




    
