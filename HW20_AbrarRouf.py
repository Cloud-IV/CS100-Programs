# Abrar Rouf
# CS 100 2017F Section H01
# HW 20, Dec 12, 2017

# 2015F Final

# a e e d c a b c e d

# Problem 11A
import turtle
turt = turtle.Turtle()
screen = turtle.Screen()


def tri(t, sideLen):
    t.pd()
    for i in range(3):
        t.fd(sideLen)
        t.lt(120)


# Problem 11B
def tris(t, initial, incr, num, angle):
    for i in range(num):
        tri(turt, initial)
        initial += incr
        t.lt(angle)


# Problem 12
def wordsByLine(inFile, outFile):
    with open(inFile, 'r') as f_in:
        f_out = open(outFile, 'w')
        lines = f_in.readlines()
        for line in lines:
            word_tracker = []
            words = line.split()
            for word in words:
                freq = line.count(word)
                if word not in word_tracker:
                    f_out.write('%s:%d ' % (word, freq))
                    word_tracker.append(word)
                elif word in word_tracker:
                    continue
            if line[-1] == '\n':
                f_out.write('\n')
    f_out.close()


# Problem 13
def lineIndex(fName):
    d = {}
    line_number = -1
    with open(fName, 'r') as f_in:
        for line in f_in:
            line_number += 1
            words = line.split()
            for word in words:
                if word not in d:
                    d[word] = [line_number]
                elif word in d:
                    if line_number not in d[word]:
                        d[word] += [line_number]
    return d
