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


class Elf(Race):
    ''' Elves '''
    def __init__(self):
        self.name = "Elf"
        self.plural = "Elves"
        self.alignment = "Neutral"
        self.darkvision = True


class Halfling(Race):
    ''' Halflings '''
    def __init__(self):
        self.name = "Halfling"
        self.plural = "Halflings"
        self.alignment = "Neutral"
        self.darkvision = False


class Gnome(Race):
    ''' Gnomes '''
    def __init__(self):
        self.name = "Gnome"
        self.plural = "Gnomes"
        self.alignment = "Neutral"
        self.darkvision = True


class Orc(Race):
    ''' Orcs '''
    def __init__(self):
        self.name = "Orc"
        self.plural = "Orcs"
        self.alignment = "Chaotic"
        self.darkvision = True


class Goblin(Race):
    ''' Goblins '''
    def __init__(self):
        self.name = "Goblin"
        self.plural = "Goblins"
        self.alignment = "Chaotic"
        self.darkvision = True


class Drow(Race):
    ''' Drow '''
    def __init__(self):
        self.name = "Drow"
        self.plural = "Drow"
        self.alignment = "Chaotic"
        self.darkvision = True


class Troll(Race):
    ''' Trolls '''
    def __init__(self):
        self.name = "Troll"
        self.plural = "Trolls"
        self.alignment = "Chaotic"
        self.darkvision = True

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
