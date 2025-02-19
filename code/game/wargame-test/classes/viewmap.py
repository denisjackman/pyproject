''' this is the world map class'''
from .map import Map


class ViewMap(Map):
    ''' World map class '''

    def __init__(self, width, height, x, y):
        super().__init__(width, height)
        self.orginX = x
        self.originY = y
