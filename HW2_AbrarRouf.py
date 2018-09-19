# Abrar Rouf
# CS 100 2017F Section H01
# HW 0, Sept 9, 2017

# Imports modules to be used in completing tasks
import turtle
import math

# Sets up screen and turtles
screen = turtle.Screen()
turt = turtle.Turtle()

# 1.
def eqTriangle(t):
    '''Draws an equilateral triangle with side length 100 using turtle t.'''
    for i in range(3):
        t.fd(100)
        t.lt(120)

def square(t):
    '''Draws a square of side length 100 using turtle t.'''
    for i in range(4):
        t.fd(100)
        t.lt(90)

def regPentagon(t):
    '''Draws a regular pentagon of side length 100 using turtle t.'''
    for i in range(5):
        t.fd(100)
        t.lt(72)

eqTriangle(turt)
square(turt)
regPentagon(turt)

# Clears screen and resets turtle 1's position
turt.reset()

# 2.
def circle_rad50(t):
    '''Draws a circle with quartercircles of radius 50, where n is the number of sides that
    make up each quartercircle, angle is the curvature of each quartercircle, and length is
    the length of each n side.'''
    circumference = (2*math.pi*50)/4
    n = int(circumference/3)+1 #  adjusts n according to circumference of circle
    angle = 90/n
    length = circumference/n
    t.pu()
    t.fd(50)
    t.pd()
    t.lt(90)
    for rep in range(4):
        for i in range(n):
            t.fd(length)
            t.lt(angle)
    turt.pu()
    turt.lt(90)
    turt.fd(50)
    turt.rt(180)
    
circle_rad50(turt)

def circle_rad100(t):
    '''Draws a circle with quartercircles of radius 100 with aforementioned variable
    assignments.'''
    circumference = (2*math.pi*100)/4
    n = int(circumference/3)+1 
    angle = 90/n
    length = circumference/n
    t.pu()
    t.fd(100)
    t.pd()
    t.lt(90)
    for rep in range(4):
        for i in range(n):
            t.fd(length)
            t.lt(angle)
    turt.pu()
    turt.lt(90)
    turt.fd(100)
    turt.rt(180)
    
circle_rad100(turt)

def circle_rad150(t):
    '''Draws a circle with quartercircles of radius 150 with aforementioned variable
    assignments.'''
    circumference = (2*math.pi*150)/4
    n = int(circumference/3)+1 
    angle = 90/n
    length = circumference/n
    t.pu()
    t.fd(150)
    t.pd()
    t.lt(90)
    for rep in range(4):
        for i in range(n):
            t.fd(length)
            t.lt(angle)
    turt.pu()
    turt.lt(90)
    turt.fd(150)
    turt.rt(180)
    
circle_rad150(turt)

def circle_rad200(t):
    '''Draws a circle with quartercircles of radius 200 with aforementioned variable
    assignments.'''
    circumference = (2*math.pi*200)/4
    n = int(circumference/3)+1 
    angle = 90/n
    length = circumference/n
    t.pu()
    t.fd(200)
    t.pd()
    t.lt(90)
    for rep in range(4):
        for i in range(n):
            t.fd(length)
            t.lt(angle)
    turt.pu()
    turt.lt(90)
    turt.fd(200)
    turt.rt(180)

circle_rad200(turt)

# 3a.
print(math.factorial(100))

print('\n')

# 3b.
print(math.log2(1000000))

print('\n')

# 3c.
print(math.gcd(49, 63))

