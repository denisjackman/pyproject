''' this is the world map class'''
from .map import Map


class WorldMap(Map):
    ''' World map class '''

    def __init__(self, width, height):
        super().__init__(width, height)
        self.name = 'World Map'
