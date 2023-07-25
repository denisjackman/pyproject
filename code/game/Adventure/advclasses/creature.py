'''
    this is a placeholder for a creature class
'''
class Creature:
    '''
        creature class
    '''
    def __init__(self):
        raise NotImplementedError("Do Not create raw Creature objects")

    def __str__(self):
        return self.name

    def can_fly(self):
        '''
            can this creature fly
        '''
        return self.fly

class Bat(Creature):
    ''' Bat '''
    def __init__(self):
        self.name = "Bat"
        self.fly = True
class Bee(Creature):
    ''' Bees '''
    def __init__(self):
        self.name = "Bee"
        self.fly = True
class GiantAnt(Creature):
    ''' Giant Ant '''
    def __init__(self):
        self.name = "Giant Ant"
        self.fly = False
class Rat(Creature):
    ''' Rat '''
    def __init__(self):
        self.name = "Rat"
        self.fly = False
class Scorpion(Creature):
    ''' Scorpion '''
    def __init__(self):
        self.name = "Scorpion"
        self.fly = False

    # Bat,True
    # Bees,True
    # Giant Ant
    # Rat
    # Scorpion
    # Slug
    # Spider
    # Snake
    # Wolf
    # Wasps,True
