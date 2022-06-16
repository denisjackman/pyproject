#!/usr/bin/env python
"""
test.py
    this is a test bed for trying pygame out prior to folding it
    in elsewhere.

References:
 https://realpython.com/pygame-a-primer/
 https://stackoverflow.com/questions/18067219/pygame-image-screen-fill

"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.0 $"
__date__ = "$Date: 2022/06/15 16:38:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
import random
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


class Player(pygame.sprite.Sprite):  # pylint: disable=R0903
    '''
        this is a class to handle player sprites
        Define a Player object by extending pygame.sprite.Sprite
        The surface drawn on the screen is now an attribute of 'player'
    '''
    def __init__(self):
        '''
            this initiates the player class
        '''
        super().__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        '''
            This helps handle pressed keys
        '''
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        # Keep player on the screen
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, SCREEN_WIDTH)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, SCREEN_HEIGHT)
        # if self.rect.left < 0:
        #     self.rect.left = 0
        # if self.rect.right > SCREEN_WIDTH:
        #    self.rect.right = SCREEN_WIDTH
        # if self.rect.top <= 0:
        #    self.rect.top = 0
        # if self.rect.bottom >= SCREEN_HEIGHT:
        #    self.rect.bottom = SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):  # pylint: disable=R0903
    '''
        this is a class to handle player sprites
        Define the enemy object by extending pygame.sprite.Sprite
        The surface you draw on the screen is now an attribute of 'enemy'
    '''
    def __init__(self):
        '''
            this initiates the enemy class
        '''
        super().__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        '''
            this updates the sprite
        '''
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


def main():
    '''
        this is the main routine
    '''
    pygame.init()
    # image = pygame.image.load("oreg.PNG")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a custom event for adding a new enemy
    add_enemy = pygame.USEREVENT + 1
    pygame.time.set_timer(add_enemy, 250)

    # Instantiate player. Right now, this is just a rectangle.
    player = Player()

    # Create groups to hold enemy sprites and all sprites
    # - enemies is used for collision detection and position updates
    # - all_sprites is used for rendering
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # surf = pygame.Surface((50, 50))
    # surf.fill(BLACK)
    # rect = surf.get_rect()
    # surf_center = (
    #                (SCREEN_WIDTH - surf.get_width()) / 2,
    #                (SCREEN_HEIGHT - surf.get_height()) / 2
    #                )
    # screen.blit(image, (0, 0))
    # pygame.draw.circle(screen, BLUE, (250, 250), 75)
    # pygame.draw.circle(screen, WHITE, (250, 250), 70)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            elif event.type == QUIT:
                running = False

            # Add a new enemy?
            elif event.type == add_enemy:
                # Create the new enemy and add it to sprite groups
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()
        # Update the player sprite based on user keypresses
        player.update(pressed_keys)
        # Update enemy position
        enemies.update()

        screen.fill((BLACK))

        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        pygame.display.flip()
        pygame.display.update()


if __name__ == '__main__':
    main()
