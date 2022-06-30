#!/usr/bin/env python
'''
    lesson 1-2
'''
import pygame
import random
from pygame.locals import *
import os

# This is a pygame template skeleton for a pygame project

# Basic Constants
WIDTH = 800
HEIGHT = 600
FPS = 30
CAPTION = "Sprite Example"

# Color Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


class Player(pygame.sprite.Sprite):
    '''
        player class
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

    def update(self):
        '''
            update method
        '''
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

def main():
    '''
        initialise pygame and set up the screen
    '''
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(CAPTION)
    clock = pygame.time.Clock()
    running = True
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    # main game loop
    while running:
        # keep loop running at the right speed
        clock.tick(FPS)
        # process input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # update
        all_sprites.update()


        # render
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # flip the display always do this last
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    # run the main routine
    main()
