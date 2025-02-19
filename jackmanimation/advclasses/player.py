'''
    player object
'''


class Player:
    '''
        player class
    '''
    def __init__(self):
        raise NotImplementedError("Do not create raw Player Objects")

    def __str__(self):
        '''
            what is my name
        '''
        return self.name

    def amount(self):
        '''
            how much gold do I have
        '''
        return self.gold

    def isRace(self):
        ''' Which race am I '''
        return self.race.name


class GamePlayer(Player):
    '''
        Game Player class
    '''
    def __init__(self):
        self.name = ""
        self.playerclass = ""
        # this will be the professions (Warrior, wizard, rogue etc)
        self.race = ""
        self.level = 1
        self.strength = 0
        self.intelligence = 0
        self.luck = 0
        self.constitution = 0
        self.dexterity = 0
        self.charisma = 0
        self.additional = 0
        self.height = 0
        self.weight = 0
        self.gold = 0
        self.experience = 0
        self.weapons = []
        self.armour = []

    # name = ""
    # type = ""  # this will be the professions (Warrior, wizard, rogue etc)
    # race = ""  # Kin: Race: This will one of the racial types as outlines
    #            in the race list
    # level = 1  # level always starts at 1
    # strength = 0
    # intelligence = 0
    # luck = 0
    # constitution = 0
    # dexterity = 0
    # charisma = 0
    # additional = 0
    # height = 0
    # weight = 0
    # weight_possible = 0
    # weight_carried = 0
    # gold = 0
    # experience = 0
    # weapons = []
    # armour = []
    # languages = []
    # magic = ""
    # other = []
