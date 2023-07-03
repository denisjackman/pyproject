''' Alien class'''
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initalise the alien and set it's starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set it's rect attribute.
        self.image = pygame.image.load('y:/Resources/development/alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien at the top left corner of the screen.
        self.rect.x = 0
        self.rect.y = 0

        # Store aliens exact horizontal position.
        self.x = float(self.rect.x)

        # will use pygame method that automatically draws all the elements of the group to the screen.
