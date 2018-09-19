# Abrar Rouf
# CS 100 2017F Section H01
# HW 9, Oct 16, 2017


# Problem 1.
def file_copy(in_file, out_file):
    """Takes an existing text file as input and copies its contents into a new file."""
    template_file = open(in_file)
    temp_file_contents = template_file.read()
    copy_file = open(out_file, 'w')
    copy_file.write(temp_file_contents)
    template_file.close()
    copy_file.close()


# Problem 2.
def file_stats(in_file):
    """Take an existing text file as input and outputs number of lines, words, and characters in text file."""
    import string
    f_in = open(in_file)
    word_list = []
    line_counter = 0
    char_counter = 0
    for line in f_in:
        line_counter += 1
        split_lines = line.split()
        words = [word.strip(string.punctuation) for word in split_lines]
        word_list += words
    for word in word_list:
        char_counter += len(word)
    print('Number of lines in %s:' % in_file, '{:>7d}'.format(line_counter))
    print('Number of words in %s:' % in_file, '{:>7d}'.format(len(word_list)))
    print('Number of characters in %s:' % in_file, char_counter)
    f_in.close()


# Problem 3.
def repeat_words(in_file, out_file):
    """Takes an existing text file as input and outputs a text file that has repeated words from the input file on the
    same line.
    """
    import string
    f_in = open(in_file)
    f_out = open(out_file, 'w')
    lines = f_in.readlines()
    newlineless_line = [line.strip('\n') for line in lines]
    clean_line = [line.strip(string.punctuation) for line in newlineless_line]
    lowercase_line = [line.lower() for line in clean_line]
    split_lines = [line.split() for line in lowercase_line]
    for line in split_lines:
        seen_words = []
        dupe_words = []
        print(line)
        for word in line:
            if word in seen_words:
                if word not in dupe_words:
                    dupe_words += [word]
            else:
                seen_words += [word]
        f_out.write('%s\n' % dupe_words)
