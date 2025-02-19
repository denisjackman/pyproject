''' ship class '''
import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        # when we initalise Ship class in the AlienInvasion class,
        # ai_game = self, which refers to the current instance of
        # Alien Invasion. Gives ship access to game resources.
        """Initalise the ship and set it's starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship and get its rect.
        self.image = pygame.image.load('Z:/Resources/development/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        # Here we manipulate the rect attribute to desired position
        # in the context of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Horizontal position of ship
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ships movement based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object after adjusting x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
