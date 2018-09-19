# Abrar Rouf
# CS 100 2017F Section H01
# HW 9, Oct 16, 2017

# Problem 1.


def twoWords(length, firstLetter):
    rtnList = []
    while True:
        firstWord = input('Please enter a word %i characters long.\n' % length)
        if len(firstWord) == length:
            rtnList.append(firstWord)
            break
        else:
            continue
    while True:
        secondWord = input('Please enter a word that starts with %s, either uppercase or lowercase.\n' % firstLetter)
        lowerFirstLetter = firstLetter.lower()
        upperFirstLetter = firstLetter.upper()
        if secondWord[0] == lowerFirstLetter:
            rtnList.append(secondWord)
            break
        elif secondWord[0] == upperFirstLetter:
            rtnList.append(secondWord)
            break
        else:
            continue
    return rtnList


# Problem 2.


def twoWordsV2(length, firstLetter):
    rtnList = []
    firstWord = input('Please enter a word %i characters long.\n' % length)
    while len(firstWord) != length:
        firstWord = input('Please enter a word %i characters long.\n' % length)
    rtnList.append(firstWord)
    secondWord = input('Please enter a word that starts with %s, either uppercase or lowercase.\n' % firstLetter)
    lowerFirstLetter = firstLetter.lower()
    upperFirstLetter = firstLetter.upper()
    while secondWord[0] != lowerFirstLetter and secondWord[0] != upperFirstLetter:
        secondWord = input('Please enter a word that starts with %s, either uppercase or lowercase.\n' % firstLetter)
    rtnList.append(secondWord)
    return rtnList


# Problem 3.


def enterNewPassword():
    userPassword = input('Please enter a password 8-15 characters long, with at least one digit.\n')
    while not any(element.isdigit() for element in userPassword):
        print('Please check your password has at least one digit in it.\n')
        userPassword = input('Please input a valid password.\n')
    while len(userPassword) < 8 or len(userPassword) > 15:
        print('Please check the length of your password and make sure it is 8-15 characters long.\n')
        userPassword = input('Please enter a valid password.\n')
    while len(userPassword) < 8 or len(userPassword) > 15 or userPassword and not any(element.isdigit() for element in userPassword):
        print('Please check your password and make sure it is 8-15 characters long, and contains at least one digit.\n')
        userPassword = input('Please enter a valid password.\n')


# Problem 4.


def guessNumber():
    import random
    randomNumber = random.randint(0, 51)
    guessCounter = 1
    userGuess = int(input("I'm thinking of a random number... You have 5 tries to guess it! What is your first guess?\n"))
    while userGuess != randomNumber:
        if guessCounter == 5:
            print('You are out of tries! The number I was thinking of was %i. Better luck next time!\n' % randomNumber)
            break
        elif userGuess > randomNumber:
            print('%i is too high.\n' % userGuess)
            guessCounter += 1
            userGuess = int(input('Try again! (Guess %i of 5)\n' % guessCounter))
        elif userGuess < randomNumber:
            print('%i is too low.\n' % userGuess)
            guessCounter += 1
            userGuess = int(input('Try again! (Guess %i of 5)\n' % guessCounter))
    print('Congratulations, you guessed correctly! It took you %i tries.' % guessCounter)
