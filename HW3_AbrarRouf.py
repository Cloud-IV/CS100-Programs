# Abrar Rouf
# CS 100 2017F Section H01
# HW 3, Sept 18, 2017

# 1. & 2.
a = 3
b = 4
c = 5

if a < b:
    print('OK')
else:
    print('NOT OK')

if c < b:
    print('OK')
else:
    print('NOT OK')

if a + b == c:
    print('OK')
else:
    print('NOT OK')

if a**2 + b**2 == c**2:
    print('OK')
else:
    print('NOT OK')

# 3.
import turtle

shape_type = input('Do you want a line, triangle, or square?\n')
color_choice = input('What color should the shape be?\n')
line_width = input('What is the line width of the shape?\n')
line_length = input('What is the line length of the shape?\n')

screen = turtle.Turtle()
turt = turtle.Turtle()


def line(color, width, length):
    #  Draws a line of specified color, width, and length with turtle left at origin.
    turt.pen(pencolor=color, pensize=width)
    turt.fd(int(length))
    turt.goto(0, 0)


def triangle(color, width, length):
    #  Draws a triangle of specified color, width, and side length with turtle left at origin.
    turt.pen(pencolor=color, pensize=width)
    for i in range(3):
        turt.fd(int(length))
        turt.lt(120)
    turt.goto(0, 0)


def square(color, width, length):
    # Draws a triangle of specified color, width, and side length with turtle left at origin.
    turt.pen(pencolor=color, pensize=width)
    for i in range(4):
        turt.fd(int(length))
        turt.lt(90)
    turt.goto(0, 0)


if shape_type == 'line':
    line(color_choice, line_width, line_length)
elif shape_type == 'triangle':
    triangle(color_choice, line_width, line_length)
elif shape_type == 'square':
    square(color_choice, line_width, line_length)
else:
    print('Please check your spelling or choose only either a line, triangle, or square and restart program.')

print('Restart program to draw another shape.')

turtle.mainloop()
