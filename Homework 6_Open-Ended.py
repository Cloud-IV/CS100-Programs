# Question 11A.
import turtle
s = turtle.Screen()
turt = turtle.Turtle()

def concentric(t, radius):
    t.pu()
    t.rt(90)
    t.fd(radius)
    t.lt(90)
    t.pd()
    t.circle(radius)
    t.pu()
    t.home()

# Question 11B.
def dartboard(turt, numRings, delta):
    radius = delta
    for i in range(int(numRings)):
        concentric(turt, radius)
        radius += delta

# Question 12.
def strLenParity(stringList):
    evenCounter = 0
    oddCounter = 0
    for list in range(len(stringList)):
        listLength = len(stringList[list])
        if listLength % 2 == 0:
            evenCounter += 1
        elif listLength % 2 == 1:
            oddCounter += 1
    returnList = [evenCounter, oddCounter]
    print(returnList)

# Question 13.
def nameLenComment(short, long):
    userName = input('What is your name?\n')
    nameLength = len(userName)
    if nameLength <= short:
        print('%s, your name is short.' % userName)
    elif nameLength >= long:
        print('%s, your name is long.' % userName)
    else:
        print('%s, your name is average.' % userName)
    print(userName)


    

    



