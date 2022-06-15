#!/usr/bin/env python
"""
test.py
    this is a test bed for trying pygame out prior to folding it
    in elsewhere.
"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.0 $"
__date__ = "$Date: 2022/06/15 16:38:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

# https://stackoverflow.com/questions/18067219/pygame-image-screen-fill
import pygame


def main():
    '''
        this is the main routine
    '''
    pygame.init()
    image = pygame.image.load("oreg.PNG")
    white = (255, 255, 255)
    width = 843
    height = 798

    screen = pygame.display.set_mode((width, height))
    screen.fill((white))

    screen.fill((white))
    screen.blit(image, (0, 0))
    pygame.display.flip()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                    break
        if done:
            break
        pygame.display.update()


if __name__ == '__main__':
    main()
