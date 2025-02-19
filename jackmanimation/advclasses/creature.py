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

    def plural_name(self):
        '''
            what is the plural name of this creature
        '''
        return self.plural


class Bat(Creature):
    ''' Bat '''
    def __init__(self):
        self.name = "Bat"
        self.fly = True
        self.plural = "Bats"


class Bee(Creature):
    ''' Bees '''
    def __init__(self):
        self.name = "Bee"
        self.fly = True
        self.plural = "Bees"


class GiantAnt(Creature):
    ''' Giant Ant '''
    def __init__(self):
        self.name = "Giant Ant"
        self.fly = False
        self.plural = "Giant Ants"


class Rat(Creature):
    ''' Rat '''
    def __init__(self):
        self.name = "Rat"
        self.fly = False
        self.plural = "Rats"


class Scorpion(Creature):
    ''' Scorpion '''
    def __init__(self):
        self.name = "Scorpion"
        self.fly = False
        self.plural = "Scorpions"


class Slug(Creature):
    ''' Slug '''
    def __init__(self):
        self.name = "Slug"
        self.fly = False
        self.plural = "Slugs"


class Spider(Creature):
    ''' Spider '''
    def __init__(self):
        self.name = "Spider"
        self.fly = False
        self.plural = "Spiders"


class Snake(Creature):
    ''' Snake '''
    def __init__(self):
        self.name = "Snake"
        self.fly = False
        self.plural = "Snakes"


class Wolf(Creature):
    ''' Wolf '''
    def __init__(self):
        self.name = "Wolf"
        self.fly = False
        self.plural = "Wolves"


class Wasp(Creature):
    ''' Wasp '''
    def __init__(self):
        self.name = "Wasp"
        self.fly = True
        self.plural = "Wasps"

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
