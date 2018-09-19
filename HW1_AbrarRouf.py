# Abrar Rouf
# CS 100 2017F Section H01
# HW 0, Sept 11, 2017

# 2. 
grades = ['A', 'B', 'C', 'D', 'F', 'D', 'C', 'B', 'A', 'A']

freqA = grades.count('A')
freqB = grades.count('B')
freqC = grades.count('C')
freqD = grades.count('D')
freqF = grades.count('F')

frequency = [freqA, freqB, freqC, freqD, freqF]
print (frequency)

# 3A.
dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']

# 3B.
herding_dogs = dog_breeds[:2]
print(herding_dogs)

# 3C.
tiny_dogs = [dog_breeds[3]]
print(tiny_dogs)

#3D.
if 'Persian' in dog_breeds:
    print(True)
else:
    print(False)




