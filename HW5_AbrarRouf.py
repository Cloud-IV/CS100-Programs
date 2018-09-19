# Abrar Rouf
# CS 100 2017F Section H01
# HW 5, Sept 25, 2017

# 1a.


def hasFinalLetter(strList, letters):
    return_list = []
    for word in strList:
        final_letter = word[-1]
        if final_letter in letters:
            return_list.append(word)
    print(return_list)


# 1b.
fruitList = ['apple', 'banana', 'cranberry', 'durian', 'eggplant']
vowels = 'aeiouyAEIOUY'
hasFinalLetter(fruitList, vowels)

monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December']
suffixes = 'yr'
hasFinalLetter(monthList, suffixes)

acronymList = ['FBI', 'CIA', 'MLB', 'NBA', 'NFL']
upperCase = 'UPPER'
hasFinalLetter(acronymList, upperCase)

# 2a.


def isDivisible(maxInt, twoInts):
    return_list = []
    for i in range(int(maxInt)):
        if i % twoInts[0] == 0 and i % twoInts[1] == 0:
            return_list.append(i)
    print(return_list)


# 2b.
maxOne = 100
tupleOne = (2, 5)
isDivisible(maxOne, tupleOne)

maxTwo = 27
tupleTwo = (3, 9)
isDivisible(maxTwo, tupleTwo)

maxThree = 0
tupleThree = (11, 13)
isDivisible(maxThree, tupleThree)
