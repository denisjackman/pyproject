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
#img_one = imgload.get_rect(0, 0, 30, 30)

pygame.display.set_caption(CAPTION)
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

def sprite(sprite_surface, sx, sy):
    '''
        sprite function
    '''
    game_screen.blit(sprite_surface, (sx, sy))


def main():
    '''
        main routine
    '''
    imgload.set_colorkey(BLACK)
    sprite_img = pygame.Surface((30, 30))
    sprite_img.set_colorkey(BLACK)
    sprite_img.blit(imgload, (0, 0), (5, 5, 35, 35))

    sprite_img2 = pygame.Surface((30, 30))
    sprite_img2.set_colorkey(BLACK)
    sprite_img2.blit(imgload, (0, 0), (5, 170, 35, 170 + 35))

    sprite_img3 = pygame.Surface((30, 30))
    sprite_img3.set_colorkey(BLACK)
    sprite_img3.blit(imgload, (0, 0), (35 + 2, 5, 37+30, 35))


    RUNNING = True

    while RUNNING:
        game_screen.fill(WHITE)
        sprite(sprite_img, 0, 0)
        sprite(sprite_img2, 60, 0)
        sprite(sprite_img3, 90, 0)

        #game_screen.blit(sprite_img, (0, 0))
        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    RUNNING = False
            elif event.type == QUIT:
                RUNNING = False
    pygame.quit()


if __name__ == '__main__':
    main()
