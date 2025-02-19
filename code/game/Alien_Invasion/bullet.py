''' bullet class '''
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from a ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ships current position."""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.colour = self.settings.bullet_colour

        # Create bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(
            0,
            0,
            self.settings.bullet_width,
            self.settings.bullet_height,
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        #  pylint: disable=w0221
        """Move the bullet up the screen."""
        self.y -= self.settings.bullet_speed

        # Update the rect value
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)
