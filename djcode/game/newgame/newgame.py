'''
    A test for a pygame
'''
from os import environ
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)  # pylint: disable=C0413
import pygame  # pylint: disable=C0413

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CAPTION = 'New Game'
SCREEN_SIZE = (WIDTH, HEIGHT)
IMG_FILE = 'y:/Resources/images/match3_db16_2.png'
IMG_FILE_2 = 'y:/Resources/images/match3_sheet_0.png'
ICON_FILE = 'y:/Resources/images/Jack.png'
SPRITE_X = 0
SPRITE_Y = 0
START_POSX = 0
START_POSY = 0
SPRITE_WIDTH = 40
SPRITE_HEIGHT = 40
sprite_size = (SPRITE_WIDTH, SPRITE_HEIGHT)
NU_SPRITE_WIDTH = 16
NU_SPRITE_HEIGHT = 16
nu_sprite_size = (NU_SPRITE_WIDTH, NU_SPRITE_HEIGHT)

pygame.init()

game_screen = pygame.display.set_mode(SCREEN_SIZE)
icon = pygame.image.load(ICON_FILE)

second_set = pygame.image.load(IMG_FILE).convert()

pygame.display.set_caption(CAPTION)
pygame.display.set_icon(icon)

clock = pygame.time.Clock()


def sprite(sprite_surface, sprite_position):
    '''
        sprite function
    '''
    sprite_surface.set_colorkey(BLACK)
    game_screen.blit(sprite_surface, sprite_position)


def sprite_load(source_surface,
                sprite_position,
                nir_sprite_size):
    '''
        new sprite image
    '''
    nu_sprite = pygame.Surface(nir_sprite_size)
    nu_sprite.set_colorkey(BLACK)
    nu_sprite.blit(source_surface,
                   (0, 0),
                   sprite_position)
    return nu_sprite


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
        pygame.draw.line(game_screen, BLACK, (100, 100), (200, 200))
        pygame.draw.line(game_screen, RED, (110, 100), (210, 200))
        pygame.draw.line(game_screen, GREEN, (120, 100), (220, 200))
        pygame.draw.line(game_screen, BLUE, (130, 100), (230, 200))
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()


if __name__ == '__main__':
    game_main()
