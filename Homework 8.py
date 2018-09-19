# Multiple-choice answers:
# e b c b c a c a b e

# Question 11A
import turtle
s = turtle.Screen()
turt = turtle.Turtle()

def drawSquare(t, length):
    t.pd()
    for i in range(4):
        t.fd(length)
        t.rt(90)

# Question 11B
def drawSquares(t, size, num, angle):
    for i in range(num):
        drawSquare(t, size)
        t.lt(angle)

# Question 12
def bigCount(numList, threshold):
    bigCounter = 0
    for element in numList:
        if element > threshold:
            bigCounter += 1
    return bigCounter

# Question 13
def getDate(message):
    month = input('What month is it?\n')
    day = input('What number day is it?\n')
    print(month, day, message)
    return print(month, day)

