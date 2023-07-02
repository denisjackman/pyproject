'''
    this is a placeholder for a creature class
'''
class Creature:
    '''
        creature class
    '''
    def __init__(self, name, fly = False):
        self.name = name
        self.fly = fly

    def __str__(self):
        return self.name

    def can_fly(self):
        '''
            can this creature fly
        '''
        return self.fly

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
