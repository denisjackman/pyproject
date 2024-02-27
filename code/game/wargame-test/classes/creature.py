''' This is a generic creature class.
    It is used to create all the creatures in the game. '''
import pygame

generic_creature = pygame.image.load(r'game-assets/images/generic.png')


class Creature:
    ''' generic creature class '''
    def __init__(self,
                 creaturename='generic creature',
                 alignment='neutral',
                 movement=36,
                 defence=1,
                 power=.05,
                 agility=.80,
                 attacks=1,
                 maxmagic=0,
                 morale=5,
                 special=None,
                 image=None):
        self.name = creaturename
        self.alignment = alignment
        self.movement = movement  # in feet
        self.defence = defence
        self.power = power
        self.agility = agility
        self.attacks = attacks
        self.maxmagic = maxmagic
        self.morale = morale
        self.special = special
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()

    def draw(self, window):
        ''' draw the creature '''

    def move(self, x, y):
        ''' move the creature '''

    def isAlignment(self):
        ''' return the alignment '''
        return self.alignment

    def isName(self):
        ''' return the name '''
        return self.name
