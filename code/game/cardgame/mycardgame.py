'''
    a card game implementation
'''
import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame as pg  # pylint: disable=C0413

FILE_LOCATION = 'Z:/Resources/development/cardgame/image/cards'
BACK_LOCATION = 'Z:/Resources/development/cardgame/image/backs/back-side.png'
SCREEN_SIZE = (1200, 800)
SCREEN_COLOR = (230, 230, 230)
SPRITE_SIZE = (64, 64)


def run_game():
    ''' main game loop '''

    pg.init()

    screen = pg.display.set_mode(SCREEN_SIZE)
    screen.fill(SCREEN_COLOR)
    screen_rect = screen.get_rect()
    image1 = pg.image.load(BACK_LOCATION)
    back = pg.transform.scale(image1, SPRITE_SIZE)
    back_rect = back.get_rect()
    back_rect.center = screen_rect.center

    pg.display.set_caption('Card Game')
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        screen.blit(back, (0, 0))

        pg.display.flip()


def main():
    ''' main function '''
    run_game()


if __name__ == '__main__':
    main()
