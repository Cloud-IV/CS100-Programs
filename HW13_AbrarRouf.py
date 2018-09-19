# Abrar Rouf
# CS 100 2017F Section H01
# HW 13, Oct 30, 2017

# F2016 Multiple-choice

# a c d d e a b e c d

# F2015 Open-ended

# Question 11A
import turtle
screen = turtle.Screen()
turt = turtle.Turtle()


def cup(t, sideLength):
    for i in range(3):
        t.pd()
        t.fd(sideLength)
        t.lt(90)
    t.up()
    t.lt(90)
    for i in range(3):
        t.fd(sideLength)
        t.rt(90)
    t.rt(90)


# Question 11B
def cups(t, initial, incr, reps):
    t.pu()
    for i in range(reps):
        t.rt(90)
        t.fd(incr/2)
        t.lt(90)
        cup(t, initial)
        initial += incr


# Question 12
def uniqueWords(inFile, outFile):
    import string
    with open(inFile) as text_file:
        count_file = open(outFile, 'w')
        text_lines = text_file.readlines()
        spaceless_lines = [line.strip('\n') for line in text_lines]
        clean_lines = [line.strip(string.punctuation) for line in spaceless_lines]
        for line in clean_lines:
            split_line = line.split()
            word_count = len(split_line)
            count_file.writelines(str(word_count) + '\n')
        count_file.close()


# Question 13
def importantWords(s, threshold):
    important_dict = {}
    words = s.split()
    for word in words:
        if len(word) >= threshold:
            if word not in important_dict:
                important_dict[word] = 1
            elif word in important_dict:
                important_dict[word] += 1
    return important_dict

# F2016 Open-Ended

# Question 11A
def letterX(t, length):
    t.pd()
    t.rt(45)
    t.fd(length/2)
    t.rt(180)
    t.fd(length)
    t.lt(180)
    t.fd(length/2)
    t.lt(45)
    t.lt(45)
    t.fd(length/2)
    t.lt(180)
    t.fd(length)
    t.rt(180)
    t.fd(length/2)
    t.rt(45)


# Question 11B
def exes(t, initSize, deltaSize, separation, xNum):
    for i in range(xNum):
        letterX(t, initSize)
        t.pu()
        t.fd(separation)
        t.pd()
        initSize *= deltaSize


# Question 12
def wordLengths(text):
    length_dict = {}
    words = text.split()
    for word in words:
        if len(word) not in length_dict:
            length_dict[len(word)] = 1
        elif len(word) in length_dict:
            length_dict[len(word)] += 1
    return length_dict


# Question 13
def initVowelCount(inFile, outFile):
    import string
    vowels = 'aeiouAEIOU'
    with open(inFile) as f_in:
        write_file = open(outFile, 'w')
        lines = f_in.readlines()
        spaceless_lines = [line.strip('\n') for line in lines]
        clean_lines = [line.strip(string.punctuation) for line in spaceless_lines]
        for line in clean_lines:
            split_lines = line.split()
            vowel_counter = 0
            for word in split_lines:
                if word[0] in vowels:
                    vowel_counter += 1
            if vowel_counter != 0:
                write_file.writelines(str(vowel_counter) + '\n')
            elif vowel_counter == 0:
                write_file.write('\n')
        write_file.close()
