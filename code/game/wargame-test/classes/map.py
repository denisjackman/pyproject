''' This is the map class. It is used to create the various maps. '''


class Map:
    ''' Map class '''
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.id = None
        self.name = None

    def getWidth(self):
        ''' Returns the width of the map '''
        return self.width

    def getHeight(self):
        ''' Returns the height of the map '''
        return self.height

    def getID(self):
        ''' Returns the ID of the map '''
        return self.id

    def getName(self):
        ''' Returns the name of the map '''
        return self.name
