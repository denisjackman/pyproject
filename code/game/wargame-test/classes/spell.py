''' This is a generic creature class.
    It is used to create all the creatures in the game. '''


class Spell:
    ''' generic spell class '''

    def __init__(self,
                 spellname='generic spell',
                 magicability=1,
                 timetocast=1,
                 duration=3,
                 affected=1,
                 effect=None,
                 spellscore=.95):
        self.name = spellname
        self.magicability = magicability
        self.timetocast = timetocast  # in turns
        self.duration = duration
        self.affected = affected
        self.effect = effect
        self.spellscore = spellscore

    def isName(self):
        ''' return the name '''
        return self.name

    def isEffect(self):
        ''' return the effect '''
        return self.effect
