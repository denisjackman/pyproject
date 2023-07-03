#!/usr/bin/env python
'''
     this is a template
'''
import pygame
# This is a pygame template skeleton for a pygame project

# Basic Constants
WIDTH = 360
HEIGHT = 480
FPS = 30
CAPTION = "My Game"

# Color Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


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

    # main game loop
    while running:
        # keep loop running at the right speed
        clock.tick(FPS)
        # process input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # update
        # render
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # flip the display always do this last
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    # run the main routine
    main()
