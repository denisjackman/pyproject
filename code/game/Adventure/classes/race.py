'''
    race class
'''
class Race:
    '''
        race class
    '''
    def __init__(self, name):
        self.name = name
        self.alignment = ""

    def __str__(self):
        return self.name

    def aligned(self):
        '''
            what is my alignment
        '''
        return self.alignment
    # taken from http://www.onrpg.com/boards/threads/14942-Basic-Races-and-Classes
    # Name
    # Human
    # Dwarf
    # Elf
    # Halfling
    # Gnome
    # Orc
    # Goblin
    # Drow (or Dark Elf)
    # Troll
