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

    start_posx = 0
    start_posy = 0
    sprite_width = 40
    sprite_height = 40
    sprite_size = (sprite_width, sprite_height)

    sprite_list = []
    cur_posx = start_posx
    cur_posy = start_posy

    for _ in range(2):
        for _ in range(8):
            sprite_pos = (cur_posx,
                          cur_posy,
                          sprite_width + cur_posx,
                          sprite_height + cur_posy )
            sprite_list.append(sprite_load(imgload, sprite_pos, sprite_size))
            cur_posx += sprite_width
        cur_posy += sprite_height
        cur_posx = 0
    cur_posx = start_posx
    cur_posy = start_posy
    nu_sprite_width = 16
    nu_sprite_height = 16
    nu_sprite_size = (nu_sprite_width, nu_sprite_height)
    for _ in range(16):
        for _ in range(6):
            sprite_pos = (cur_posx,
                          cur_posy,
                          nu_sprite_width + cur_posx,
                          nu_sprite_height + cur_posy )
            sprite_img2 = sprite_load(second_set, sprite_pos, nu_sprite_size)
            sprite_list.append(pygame.transform.scale(sprite_img2, (40, 40)))
            cur_posx += nu_sprite_width
        cur_posy += nu_sprite_height
        cur_posx = 0


    RUNNING = True

    while RUNNING:
        RUNNING = check_status()
        game_screen.fill(WHITE)
        row = 0
        screen_x = 0
        screen_y = 0
        offset = 0

        for item in sprite_list:
            if row == 8:
                row = 0
                screen_x = offset
                screen_y += sprite_height


            screen_position = (screen_x, screen_y)
            sprite(item, screen_position)
            screen_x += sprite_width
            row += 1
            if screen_y > HEIGHT:
                screen_y = 0
                offset += 160
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()


if __name__ == '__main__':
    main()
