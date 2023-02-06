''' This is the tile class. It is used to create the tiles that make up the map. '''

class Tile:
    ''' Tile class'''
    def __init__(self, tileid, image, name, type):
        self.id = tileid
        self.image = image
        self.name = name
        self.passable = False
        self.type = type

    def isPassable(self):
        ''' Returns whether or not the tile is passable '''
        return self.passable

    def getType(self):
        ''' Returns the type of the tile '''
        return self.type

    def getName(self):
        ''' Returns the name of the tile '''
        return self.name
    
    def makePassable(self):
        ''' Makes the tile passable '''
        self.passable = True
        
    def makeImpassable(self):
        ''' Makes the tile impassable '''
        self.passable = False
        