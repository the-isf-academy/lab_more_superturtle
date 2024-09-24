# tree_parts.py

from turtle import *
from shapes import triangle, rectangle
from superturtle.movement import update_position

def tree_top(size, top_color):
    # draws 3 triangles on top of each other to looks like
    # the top of a tree

    for i in range(3):
        triangle(size, top_color)
        penup()
        left(90)
        forward(size/2)
        right(90)
        pendown()

def tree_trunk(width, height, trunk_color):
    # draws a rectangle with specific dimensions
    # to look like a tree trunk

    rectangle(width,height, trunk_color)

def tree_full(width, height, trunk_color, top_color):
    tree_trunk(width, height, trunk_color)
    update_position(-width//2, height)
    tree_top(width*2, top_color)

