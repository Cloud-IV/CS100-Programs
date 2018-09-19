# Abrar Rouf
# CS 100 2017F Section H01
# HW 14, Nov 5, 2017

# Multiple-choice Answers

# a b c a d e d b c e

# Open-ended

# Question 11A
import turtle
s = turtle.Screen()
turt = turtle.Turtle()


def tri(t, length):
    t.pd()
    for i in range(3):
        t.fd(length)
        t.lt(180)
        t.fd(length)
        t.lt(180)
        t.lt(120)


# Question 11B
def tris(t, initSize, ratio, rotation, num):
    for i in range(num):
        tri(turt, initSize)
        initSize *= ratio
        t.lt(rotation)


# Question 12
def initialLets(t):
    let_dict = {}
    words = t.split()
    for word in words:
        if word[0] not in let_dict:
            let_dict[word[0]] = 1
        elif word[0] in let_dict:
            let_dict[word[0]] += 1
    return let_dict


# Question 13
def initVowels(inFile, outFile):
    with open(inFile) as f_in:
        vowels = 'AEIOUaieou'
        vowel_file = open(outFile, 'w')
        lines = f_in.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                for vowel in vowels:
                    if word[0] == vowel:
                        vowel_file.writelines(word + ' ')
            if line[-1] == '\n':
                vowel_file.write('\n')
    vowel_file.close()
