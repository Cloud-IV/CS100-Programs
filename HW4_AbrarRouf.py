# Abrar Rouf
# CS 100 2017F Section H01
# HW 4, Sept 20, 2017

# 1.
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'December']

for month in months:
    firstLetter = month[0]
    if firstLetter == 'J':
        print(month)

# 2.
for i in range(100):
    if i % 2 == 0 and i % 5 == 0:
        print(i)

# 3.
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for letter in horton:
    if letter in vowels:
        print(letter)
