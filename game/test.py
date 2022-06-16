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
    RLEACCEL,
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
SKY_BLUE = (135, 206, 250)

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
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((WHITE), RLEACCEL)
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
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey(WHITE, RLEACCEL)
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


class Cloud(pygame.sprite.Sprite):  # pylint: disable=R0903
    '''
    Define the cloud object by extending pygame.sprite.Sprite
    Use an image for a better-looking sprite
    '''
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey(BLACK, RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )


def update(self):
    '''
        Move the cloud based on a constant speed
        Remove the cloud when it passes the left edge of the screen
    '''
    self.rect.move_ip(-5, 0)
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

    add_cloud = pygame.USEREVENT + 2
    pygame.time.set_timer(add_cloud, 1000)

    # Instantiate player. Right now, this is just a rectangle.
    player = Player()

    # Create groups to hold enemy sprites and all sprites
    # - enemies is used for collision detection and position updates
    # - all_sprites is used for rendering
    enemies = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    # Setup the clock for a decent framerate
    clock = pygame.time.Clock()
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

            # Add a new cloud?
            elif event.type == add_cloud:
                # Create the new cloud and add it to sprite groups
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)

        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()
        # Update the player sprite based on user keypresses
        player.update(pressed_keys)
        # Update enemy position
        enemies.update()
        clouds.update()

        screen.fill((SKY_BLUE))

        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        # Check if any enemies have collided with the player
        if pygame.sprite.spritecollideany(player, enemies):
            # If so, then remove the player and stop the loop
            player.kill()
            running = False

        pygame.display.flip()
        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)


if __name__ == '__main__':
    main()
