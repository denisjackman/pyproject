'''Empire class for Lineage game'''


class Empire:
    '''Empire class for Lineage game'''

    def __init__(self):
        self.name = "Empire"
        self.population = 1000
        self.size = 1000
        self.food = 0
        self.happieness = 0
        self.global_factors = 0
        self.local_factors = 0

    def __str__(self):
        return self.name

    def currentPopulation(self):
        ''' return the current population '''
        return self.population

    def currentSize(self):
        ''' return the current size '''
        return self.size

    def currentFood(self):
        ''' return the current food '''
        return self.food

    def updateName(self, name):
        ''' update the name '''
        self.name = name

    def updatePopulation(self, population):
        ''' update the population '''
        self.population = population

    def updateSize(self, size):
        ''' update the size '''
        self.size = size

    def updateFood(self, food):
        ''' update the food '''
        self.food = food
