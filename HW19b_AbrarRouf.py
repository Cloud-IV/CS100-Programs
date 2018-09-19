# Abrar Rouf
# CS 100 2017F Section H01
# HW 19b, Dec 10, 2017

# 2016F Final

# b c e a d a a b e d

# Problem 11a
import turtle
turt = turtle.Turtle()
screen = turtle.Screen()


def regularPoly(t, sideLen, numSides):
    t.speed(10)
    t.pd()
    for i in range(numSides):
        t.fd(sideLen)
        t.lt(360/numSides)


# Problem 11b
def increasingPolys():
    numSides = 3
    for i in range(6):
        regularPoly(turt, 100, numSides)
        numSides += 1


# Problem 12
def wordLengths(inFile, outFile):
    with open(inFile, 'r') as f_in:
        f_out = open(outFile, 'w')
        lines = f_in.readlines()
        for line in lines:
            words = line.split()
            word_lengths = []
            same_length = 0
            for word in words:
                word_length = len(word)
                word_lengths += str(word_length)
                longest_word = max(word_lengths)
                if len(word) == int(longest_word):
                    same_length += 1
            if line == '\n':
                f_out.write('\n')
            else:
                f_out.write(str(longest_word) + ' ' + str(same_length) + '\n')
    f_in.close()
    f_out.close()


# Problem 13a
def countVowels(s):
    vowels = 'aeiou'
    vowel_counter = 0
    lowercase_s = s.lower()
    for character in lowercase_s:
        if character in vowels:
            vowel_counter += 1
    return vowel_counter


# Problem 13b
def vowelFrequency(t):
    vowel_dict = {}
    words = t.split()
    for word in words:
        if countVowels(word) not in vowel_dict.keys():
            vowel_dict[countVowels(word)] = [word]
        elif countVowels(word) in vowel_dict.keys():
                vowel_dict[countVowels(word)] += [word]
    return vowel_dict


# 2017S Final

# c b e d b b d e e a

# Question 11A
def halfSquare(t, length):
    t.pd()
    for i in range(2):
        t.fd(length)
        t.lt(90)


# Question 11B
def spiral(t, increment, num):
    increase = increment
    for i in range(num):
        halfSquare(turt, increment)
        increment += increase


# Question 12
def lineStats(file_in, file_out):
    print("Sorry, I didn't finish this in time.")


# Question 13
def vowelEndings(text):
    print("Sorry again, also didn't finish this in time.")