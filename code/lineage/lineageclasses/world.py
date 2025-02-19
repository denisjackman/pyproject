'''World class for Lineage game'''


class World:
    '''World class for Lineage game'''

    def __init__(self):
        self.name = "World"
        self.width = 0
        self.height = 0
        self.map = []

    def __str__(self):
        return self.name

    def isName(self):
        '''Returns the name of the world'''
        return self.name

    def isWidth(self):
        '''Returns the width of the world'''
        return self.width

    def isHeight(self):
        '''Returns the height of the world'''
        return self.height

    def updateName(self, name):
        '''Updates the name of the world'''
        self.name = name
