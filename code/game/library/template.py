#!/usr/bin/env python
"""
test.py
    this is a test bed for trying pygame out prior to folding it
    in elsewhere.

References:


"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.0 $"
__date__ = "$Date: 2022/06/15 16:38:00 $"
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
pygame.init()


def main():
    '''
        this is the main routine
    '''

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True

    # Setup the clock for a decent framerate
    clock = pygame.time.Clock()
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
    pygame.mixer.quit()


if __name__ == '__main__':
    main()
