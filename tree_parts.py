# tree_parts.py

from turtle import *
from shapes import triangle, rectangle

def tree_top(size):
    # draws 3 triangles on top of each other to looks like
    # the top of a tree

    for i in range(3):
        triangle(size,"green")
        penup()
        left(90)
        forward(size/2)
        right(90)
        pendown()

def tree_trunk(width, height):
    # draws a rectangle with specific dimensions
    # to look like a tree trunk

    rectangle(width,height,"brown")

