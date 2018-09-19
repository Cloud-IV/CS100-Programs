# Abrar Rouf
# CS 100 2017F Section H01
# HW 12 Part 1, Oct 29, 2017

# Problem 0


def bookFreq(book_name):
    import string
    word_freq = {}
    with open(book_name) as book_file:
        text_content = book_file.read()
        words = text_content.split()
        clean_words = [word.strip(string.punctuation) for word in words]
        for clean_word in clean_words:
            if clean_word not in word_freq:
                word_freq[clean_word] = 1
            elif clean_word in word_freq:
                word_freq[clean_word] += 1
    return word_freq


# Problem 1
def initialLetterCount(wordList):
    letter_count = {}
    for word in wordList:
        if word[0] not in letter_count:
            letter_count[word[0]] = 1
        elif word[0] in letter_count:
            letter_count[word[0]] += 1
    return letter_count


# Problem 2
def initialLetters(wordList):
    word_dict = {}
    for word in wordList:
        if word[0] not in word_dict:
            word_dict[word[0]] = [word]
        elif word[0] in word_dict:
            word_dict[word[0]] += [word]
    return word_dict


# Problem 3
def shareALetter(wordList):
    shared_dict = {}
    for word_one in wordList:
        shared_dict[word_one] = set()
        for word_two in wordList:
            for character in word_two:
                if character in word_one:
                    shared_dict[word_one].update([word_two])
    return shared_dict
