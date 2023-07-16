'''
    A test for a pygame
'''
import pygame
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 1200
HEIGHT = 900
CAPTION = 'Utility Program'
SCREEN_SIZE = (WIDTH, HEIGHT)
FPS = 60

ICON_FILE = r'y:/Resources/pumpkin_dude.png'


SPRITE_X = 0
SPRITE_Y = 0
IMG_FILE = r'y:/Resources/images/stella_walk.png'
START_POSX = 0
START_POSY = 0
SPRITE_WIDTH = 64
SPRITE_HEIGHT = 64
sprite_size = (SPRITE_WIDTH, SPRITE_HEIGHT)


def sprite(sprite_surface, sprite_position):
    '''
        sprite function
    '''
    sprite_surface.set_colorkey(BLACK)
    game_screen.blit(sprite_surface, sprite_position)


def sprite_load(source_surface,
                sprite_position,
                new_sprite_size):
    '''
        new sprite image
    '''
    new_sprite = pygame.Surface(new_sprite_size)
    new_sprite.set_colorkey(WHITE)
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
    pygame.init()
    game_screen = pygame.display.set_mode(SCREEN_SIZE)
    icon = pygame.image.load(ICON_FILE)
    pygame.display.set_caption(CAPTION)
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    img = []
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_000.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_001.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_002.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_003.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_004.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_005.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_006.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_007.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_008.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_009.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_010.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_011.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_012.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_014.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_015.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_016.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_017.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_018.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_019.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_020.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_021.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_022.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_023.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_024.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_025.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_026.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_027.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_028.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_029.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_030.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_031.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_032.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_033.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_034.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_035.png').convert())
    img.append(pygame.image.load('y:/pyproject/resources/images/test/sprites/e_036.png').convert())
    newimg = []
    for item in img:
        newimg.append(pygame.transform.scale(item, (64, 64)))
    imgload = pygame.image.load(IMG_FILE).convert()

    sprite_list = []
    cur_posx = START_POSX
    cur_posy = START_POSY

    for _ in range(8):
        for _ in range(4):
            sprite_pos = (cur_posx,
                          cur_posy,
                          SPRITE_WIDTH + cur_posx,
                          SPRITE_HEIGHT + cur_posy)
            sprite_list.append(sprite_load(imgload, sprite_pos, sprite_size))
            cur_posx += SPRITE_WIDTH
        cur_posy += SPRITE_HEIGHT
        cur_posx = 0
    cur_posx = START_POSX
    cur_posy = START_POSY

    RUNNING = True
    screen_x = 300
    screen_y = 300
    screen_position = (screen_x, screen_y)
    count = 0
    counter = 0
    sprite_timer = 0

    while RUNNING:
        RUNNING = check_status()
        game_screen.fill(WHITE)
        sprite(sprite_list[count], screen_position)
        sprite(newimg[counter], (100, 300))
        sprite_timer += FPS
        if sprite_timer >= 600:
            counter += 1
            count += 1
            sprite_timer = 0
        if count >= 4:
            count = 0

        if counter >= len(img):
            counter = 0
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
