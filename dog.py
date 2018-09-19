# Abrar Rouf
# CS 100 2017F Section H01
# HW 15, Nov 26, 2017

# Problems 1-5


class Dog:
    def __init__(self, dog_name, dog_breed):
        """Creates a dog and assigns dog a name and breed."""
        self.name = dog_name
        self.breed = dog_breed
        self.tricks = []

    def teach(self, trick):
        self.tricks = trick
        print('%s knows %s.' % (self.name, self.tricks))

    def knows(self, trick):
        if trick in self.tricks:
            print('Yes, %s knows %s.' % (self.name, self.tricks))
            return True
        else:
            print('No, %s does not know %s.' % (self.name, trick))
            return False

    def species(self):
        self.species = 'Canis familiaris'
