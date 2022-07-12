'''
    A test for a pygame
'''
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame  # pylint: disable=C0413
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)  # pylint: disable=C0413

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 410
HEIGHT = 304
CAPTION = 'New Game'
SCREEN_SIZE = (WIDTH, HEIGHT)
IMG_FILE = 'y:/Resources/images/match3_sheet_0.png'
ICON_FILE = 'y:/pyproject/resources/icon.png'
SPRITE_X = 0
SPRITE_Y = 0

pygame.init()

game_screen = pygame.display.set_mode(SCREEN_SIZE)
icon = pygame.image.load(ICON_FILE)
imgload = pygame.image.load(IMG_FILE).convert()

pygame.display.set_caption(CAPTION)
pygame.display.set_icon(icon)

clock = pygame.time.Clock()


def sprite(sprite_surface, sx, sy):
    '''
        sprite function
    '''
    game_screen.blit(sprite_surface, (sx, sy))


def sprite_load(source_surface,
                sprite_position,
                sprite_size):
    '''
        new sprite image
    '''
    new_sprite = pygame.Surface(sprite_size)
    new_sprite.set_colorkey(BLACK)
    new_sprite.blit(source_surface,
                    (0, 0),
                    sprite_position)
    return new_sprite


def check_status():
    '''
        this checks the status of the game and return True is it should keep
        running False is not.
        There are no parameters to be passed and it returns a boolean as a
        response.
    '''
    result = True
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                result = False
        elif event.type == QUIT:
            result = False
    return result


def main():
    '''
        main routine
    '''
    imgload.set_colorkey(BLACK)
    sprite_img = sprite_load(imgload, (5, 5, 35, 35), (30, 30))
    sprite_img2 = sprite_load(imgload, (5, 170, 35, 205), (30, 30))
    sprite_img3 = sprite_load(imgload, (37, 5, 67, 35), (30, 30))

    RUNNING = True
    while RUNNING:
        RUNNING = check_status()
        game_screen.fill(WHITE)
        sprite(sprite_img, 0, 0)
        sprite(sprite_img2, 60, 0)
        sprite(sprite_img3, 90, 0)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()


if __name__ == '__main__':
    main()
