'''

    A test for a pygame

    references:
    Hex Grids   : https://www.redblobgames.com/grids/hexagons/
    Hex Sprites : https://opengameart.org/content/hexagon-pack-310x

'''
from os import environ
import math
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)
import pygame

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

WIDTH = 800
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)

CAPTION = 'Hex Strat Game'

ICON_FILE = 'y:/Resources/images/Jack.png'
#HEX_SHEET = 'y:/pyproject/scratch/project/hexagonAll_sheet.png'
HEX_TILE = 'y:/pyproject/scratch/project/grass_01.png'

SPRITE_X = 0
SPRITE_Y = 0
START_POSX = 0
START_POSY = 0

SPRITE_WIDTH = 60
SPRITE_HEIGHT = 70
sprite_size = (SPRITE_WIDTH, SPRITE_HEIGHT)
VERT = 3/4 * SPRITE_HEIGHT
WIDTH = math.sqrt(3) * SPRITE_HEIGHT/2

pygame.init()

game_screen = pygame.display.set_mode(SCREEN_SIZE)

icon = pygame.image.load(ICON_FILE)
#hexsprites = pygame.image.load(HEX_SHEET).convert_alpha()
grasstile = pygame.image.load(HEX_TILE).convert_alpha()
grasstile = pygame.transform.scale(grasstile, sprite_size)

pygame.display.set_caption(CAPTION)
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

def check_game_status():
    '''
        this checks the status of the game and return True is it should keep
        running False is not.
        There are no parameters to be passed and it returns a boolean as a
        response.
    '''
    game_result = True
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_result = False
        elif event.type == QUIT:
            game_result = False
    return game_result


def game_main():
    '''
        main routine
    '''
    RUNNING = True

    while RUNNING:
        RUNNING = check_game_status()
        game_screen.fill(WHITE)
        screenx = 0
        screeny = 0

        for _ in range(1, 13):
            game_screen.blit(grasstile, (screenx, screeny))
            screenx = screenx + SPRITE_WIDTH
        screenx = SPRITE_WIDTH/2
        screeny += VERT
        for _ in range(1, 13):
            game_screen.blit(grasstile, (screenx, screeny))
            screenx = screenx + SPRITE_WIDTH
        screenx = 0
        screeny += VERT
        for _ in range(1, 13):
            game_screen.blit(grasstile, (screenx, screeny))
            screenx = screenx + SPRITE_WIDTH
        screenx = SPRITE_WIDTH/2
        screeny += VERT
        for _ in range(1, 13):
            game_screen.blit(grasstile, (screenx, screeny))
            screenx = screenx + SPRITE_WIDTH
        screenx = 0
        screeny += VERT
        for _ in range(1, 13):
            game_screen.blit(grasstile, (screenx, screeny))
            screenx = screenx + SPRITE_WIDTH
        screenx = SPRITE_WIDTH/2
        screeny += VERT
        for _ in range(1, 13):
            game_screen.blit(grasstile, (screenx, screeny))
            screenx = screenx + SPRITE_WIDTH
        screenx = 0
        screeny += VERT
        for _ in range(1, 13):
            game_screen.blit(grasstile, (screenx, screeny))
            screenx = screenx + SPRITE_WIDTH
        screenx = SPRITE_WIDTH/2
        screeny += VERT
        for _ in range(1, 13):
            game_screen.blit(grasstile, (screenx, screeny))
            screenx = screenx + SPRITE_WIDTH
        screenx = 0
        screeny += VERT
        for _ in range(1, 13):
            game_screen.blit(grasstile, (screenx, screeny))
            screenx = screenx + SPRITE_WIDTH
 
 
        x,y = pygame.mouse.get_pos()
        hx = round(x / SPRITE_WIDTH)
        hy = round(y / SPRITE_HEIGHT)
        newcaption = f'Hex Strat Game - ( x: {x} y: {y} ) ( hx: {hx} hy: {hy} )'
        pygame.display.set_caption(newcaption)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()


if __name__ == '__main__':
    game_main()
