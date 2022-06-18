#!/usr/bin/env python
"""
rogue.py
    This is the basis for a rogue like game platform.

References:
https://www.gridsagegames.com/blog/2018/10/how-to-make-a-roguelike/
https://www.kenney.nl/

"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.0 $"
__date__ = "$Date: 2022/06/17 14:23:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

import pygame
from pygame.locals import (
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

# Setup for sounds. Defaults are good.
pygame.mixer.init()
pygame.init()
# Here we load the image we want to
# use
Icon = pygame.image.load('icon.png')

# We use set_icon to set new icon
pygame.display.set_icon(Icon)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def game_main():
    '''
        this is the main routine
    '''

    running = True
    pygame.display.set_caption('Rogue')
    # Setup the clock for a decent framerate
    colour = WHITE
    # pygame.title("Test Bed Pygame Primer")
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            elif event.type == QUIT:
                running = False

        screen.fill((colour))

        pygame.display.flip()
        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)
    # All done! Stop and quit the mixer.
    pygame.mixer.music.stop()


def game_intro():
    '''
        this loads the game menu an settings options
    '''
    intro_running = True
    pygame.display.set_caption('Rogue: Game Intro')
    # Setup the clock for a decent framerate
    colour = SKY_BLUE
    # pygame.title("Test Bed Pygame Primer")
    while intro_running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    intro_running = False

            elif event.type == QUIT:
                intro_running = False

        screen.fill((colour))

        pygame.display.flip()
        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)
    # All done! Stop and quit the mixer.
    pygame.mixer.music.stop()


def game_credits():
    '''
        This loads the game credits and dsiaplays them
    '''
    print("Game Credits")
    credits_running = True
    pygame.display.set_caption('GAME CREDITS')
    # Setup the clock for a decent framerate
    colour = BLACK
    # pygame.title("Test Bed Pygame Primer")
    while credits_running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    credits_running = False

            elif event.type == QUIT:
                credits_running = False

        screen.fill((colour))

        pygame.display.flip()
        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)
    # All done! Stop and quit the mixer.
    pygame.mixer.music.stop()


def main():
    '''
        this is the main game routine
    '''
    game_intro()
    game_main()
    game_credits()
    pygame.mixer.quit()


if __name__ == '__main__':
    main()
