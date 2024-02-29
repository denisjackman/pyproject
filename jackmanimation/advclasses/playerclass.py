''' Player Class object '''


class PlayerClass:
    ''' Player Class object'''
    def __init__(self):
        raise NotImplementedError("Do not create raw PlayerClass objects.")

    def __str__(self):
        ''' return the name of the class '''
        return self.name

    def isMagicUser(self):
        ''' return true if the class is a magic user '''
        return self.magicuser

    def isImmunePoison(self):
        ''' return true if the class is immune to poison '''
        return self.immune_poison


class Mage(PlayerClass):
    ''' Mage Player Class '''
    def __init__(self):
        self.name = "Mage"
        self.magicuser = True
        self.immune_poison = False
        self.plural = "Mages"


class Warrior(PlayerClass):
    ''' Warrior Player Class '''
    def __init__(self):
        self.name = "Warrior"
        self.magicuser = False
        self.immune_poison = False
        self.plural = "Warriors"
