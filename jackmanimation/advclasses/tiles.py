''' Tiles class'''


class MapTile:
    ''' Map Tile class '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = ""
        self.image = ""
        self.description = ""

    def intro_text(self):
        ''' intro text '''
        raise NotImplementedError()

    def isName(self):
        ''' name '''
        return self.name


class StartTile(MapTile):
    ''' Start Tile class '''
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Start Tile"
        self.image = "starttile.png"
        self.description = "This is the start tile"

    def intro_text(self):
        ''' intro text '''
        return '''
        You are standing in a dark cave.
        '''


class NormalTile(MapTile):
    ''' Normal Tile class '''
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Normal Tile"
        self.image = "normaltile.png"
        self.description = "This is a normal tile"

    def intro_text(self):
        ''' intro text '''
        return '''
        You are standing in a clearing.
        '''


class VictoryTile(MapTile):
    ''' Victory Tile class '''
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Victory Tile"
        self.image = "victorytile.png"
        self.description = "This is the victory tile"

    def intro_text(self):
        ''' intro text '''
        return '''
        You are victorius.
        '''
