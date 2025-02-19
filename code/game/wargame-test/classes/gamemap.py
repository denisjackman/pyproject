''' this is the world map class'''
from .map import Map


class GameMap(Map):
    ''' World map class '''
    def __init__(self, width, height, x, y):
        super().__init__(width, height)
        self.orginX = x
        self.originY = y

    def getOrigin(self):
        ''' get the origin of the map '''
        return (self.orginX, self.originY)

    def setOrigin(self, x, y):
        ''' set the origin of the map '''
        self.orginX = x
        self.originY = y
