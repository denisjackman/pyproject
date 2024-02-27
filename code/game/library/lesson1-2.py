#!/usr/bin/env python
'''
    lesson 1-2
'''
import pygame

# This is a pygame template skeleton for a pygame project

# Basic Constants
WIDTH = 900
HEIGHT = 500
FPS = 40
CAPTION = "New Sprite Example"

# Color Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    '''
        player class
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        '''
            update method for self
        '''
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

    def location(self):
        '''
            return my real current location
        '''
        return self.rect.center


def main():
    '''
        initialise pygame and set up the screen
        run the main program
    '''
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(CAPTION)
    clock = pygame.time.Clock()
    main_running = True
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    # main game loop
    while main_running:
        # keep loop main_running at the right speed
        clock.tick(FPS)
        # process input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_running = False
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
