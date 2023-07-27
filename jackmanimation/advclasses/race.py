'''
    race class
'''
class Race:
    '''
        race class
    '''
    def __init__(self):
        raise NotImplementedError("Do Not create raw Race objects")

    def __str__(self):
        return self.name

    def aligned(self):
        '''
            what is my alignment
        '''
        return self.alignmen
    def hasDarkVision(self):
        '''
            do I have darkvision
        '''
        return self.darkvision
class Human(Race):
    ''' Humans '''
    def __init__(self):
        self.name = "Human"
        self.plural = "Humans"
        self.alignment = "Any"
        self.darkvision = False

class Dwarf(Race):
    ''' Dwarves '''
    def __init__(self):
        self.name = "Dwarf"
        self.plural = "Dwarves"
        self.alignment = "Lawful"
        self.darkvision = True

    # Elf
    # Halfling
    # Gnome
    # Orc
    # Goblin
    # Drow (or Dark Elf)
    # Troll

    # taken from http://www.onrpg.com/boards/threads/14942-Basic-Races-and-Classes
    # Name
    # Human
    # Dwarf
