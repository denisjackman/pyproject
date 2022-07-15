'''
    A test for a pygame
'''
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame  # pylint: disable=C0413
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)  # pylint: disable=C0413

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CAPTION = 'New Game'
SCREEN_SIZE = (WIDTH, HEIGHT)
IMG_FILE = 'y:/Resources/images/match3_db16_2.png'
IMG_FILE_2 = 'y:/pyproject/resources/match3_tiles_px.png'
ICON_FILE = 'y:/pyproject/resources/icon.png'
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
imgload = pygame.image.load(IMG_FILE_2).convert()
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



    sprite_list = []
    nu_cur_posx = START_POSX
    nu_cur_posy = START_POSY

    for _ in range(2):
        for _ in range(8):
            sprite_pos = (nu_cur_posx,
                          nu_cur_posy,
                          SPRITE_WIDTH + nu_cur_posx,
                          SPRITE_HEIGHT + nu_cur_posy )
            sprite_list.append(sprite_load(imgload, sprite_pos, sprite_size))
            nu_cur_posx += SPRITE_WIDTH
        nu_cur_posy += SPRITE_HEIGHT
        nu_cur_posx = 0
    nu_cur_posx = START_POSX
    nu_cur_posy = START_POSY

    for _ in range(16):
        for _ in range(6):
            sprite_pos = (nu_cur_posx,
                          nu_cur_posy,
                          NU_SPRITE_WIDTH + nu_cur_posx,
                          NU_SPRITE_HEIGHT + nu_cur_posy )
            sprite_img2 = sprite_load(second_set, sprite_pos, nu_sprite_size)
            sprite_list.append(pygame.transform.scale(sprite_img2, (40, 40)))
            nu_cur_posx += NU_SPRITE_WIDTH
        nu_cur_posy += NU_SPRITE_HEIGHT
        nu_cur_posx = 0


    RUNNING = True

    while RUNNING:
        RUNNING = check_game_status()
        game_screen.fill(WHITE)
        row = 0
        screen_x = 0
        screen_y = 0
        offset = 0

        for item in sprite_list:
            if row == 8:
                row = 0
                screen_x = offset
                screen_y += SPRITE_HEIGHT


            screen_position = (screen_x, screen_y)
            sprite(item, screen_position)
            screen_x += SPRITE_WIDTH
            row += 1
            if screen_y > HEIGHT:
                screen_y = 0
                offset += 160
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()


if __name__ == '__main__':
    game_main()
