from turtle import *

def triangle(size,triangle_color):
    # draws a triangle of any size and color

    color(triangle_color)
    begin_fill()
   
    for i in range(3):
        forward(size)
        left(120)
    # left(60)
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

def filled_circle(circle_size, rgb_color):
    pencolor(rgb_color)
    fillcolor(rgb_color)
    begin_fill()
    circle(circle_size)
    end_fill()