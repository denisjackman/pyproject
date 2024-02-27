''' This is the tile class.
    It is used to create the tiles that make up the map. '''


class Tile:
    ''' Tile class'''
    def __init__(self, tileid, image, name, tiletype):
        self.id = tileid
        self.image = image
        self.name = name
        self.passable = None
        self.tiletype = tiletype
        self.selected = False

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

    def isClicked(self, mousepos):
        ''' Returns whether or not the tile is clicked '''
        if self.rect.collidepoint(mousepos):
            return True
        return False

    def draw(self, surface):
        ''' Draws the tile to the surface '''
        surface.blit(self.image, self.rect)

    def isSelected(self):
        ''' Returns whether or not the tile is selected '''
        return self.selected
