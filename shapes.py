from turtle import *

def triangle(side_len, color_name):
    color(color_name)
    begin_fill()
    for i in range(3):
        left(120)
        forward(side_len)
    end_fill()


def rectangle(width, height, color_name):
    color(color_name)
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()