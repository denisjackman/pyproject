''' This is a test game project'''
import os
import sys
from os import environ


environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE, K_LEFT, K_RIGHT)  # pylint: disable=C0413
import pygame  # pylint: disable=C0413

# pylint: disable=C0413
sys.path.append(os.path.realpath('..\\..'))
from jackmanimation.utilities.fileutility import walk_through

WIDTH = 800
HEIGHT = 600
CAPTION = 'Sprite Viewer'
SCREEN_SIZE = (WIDTH, HEIGHT)
ICON_FILE = 'Z:/Resources/logo.jpg'
GAME_RESOURCES = 'E:/development/'

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BACK_COLOR = (102, 153, 153)
STATUS_COLOR = (245, 110, 2)


def tp_check_key_status():
    '''
        this checks the status of the keys and return the value
        of the pressed key.
        There are no parameters to be passed and it returns a string as a
        response.
        Currently it returns 'Run', 'Quit', 'Left' or 'Right'
    '''
    tcks_key_result = 'Run'
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                tcks_key_result = 'Quit'
            if event.key == K_LEFT:
                tcks_key_result = 'Left'
            if event.key == K_RIGHT:
                tcks_key_result = 'Right'
        elif event.type == QUIT:
            tcks_key_result = 'Quit'
    return tcks_key_result


def main():
    """ This is the main function """
    # initialize pygame
    pygame.init()
    # set the screen size
    game_screen = pygame.display.set_mode(SCREEN_SIZE)
    # set the caption and icon
    icon = pygame.image.load(ICON_FILE)
    pygame.display.set_caption(CAPTION)
    pygame.display.set_icon(icon)
    # set the clock and fonts
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("kenneyhighregular", 24)
    sfont = pygame.font.SysFont("couriernew", 24)
    # get all the fonts available
    # uncomment the following lines to see all the fonts available
    # all_fonts = pygame.font.get_fonts()
    # for fontname in all_fonts:
    #     print(f'[-] {fontname}')
    # print(f"[-] Fonts found {len(all_fonts):,}")

    # get all the images in the directory
    totallist = []
    commands = {"verbosemode": False,
                "deletemode": False,
                "startdirectory": f'{GAME_RESOURCES}hex'}
    totallist.extend(walk_through(commands))
    # set the game status to True
    # and prepare to run the game loop
    game_status = True
    print(f"[-] Records found {len(totallist):,}")
    count = 0
    status_text = font.render("Press ESC to quit", True, BLACK)
    info_text = font.render("Press LEFT or RIGHT to navigate", True, WHITE)
    directory_text = font.render(f'{GAME_RESOURCES}hex', True, WHITE)
    while game_status:
        # this is the game loop that runs the game
        # and checks the key status
        game_state = tp_check_key_status()
        # check the key status and act accordingly
        if game_state == 'Quit':
            game_status = False
        if game_state == 'Right':
            count += 1
        if game_state == 'Left':
            count -= 1
        # check the count and reset it if it goes out of bounds
        count = max(0, count)
        count = min(count, len(totallist) - 1)
        # load the image and display it load the text and render it
        img = pygame.image.load(totallist[count])
        img_text = sfont.render(os.path.basename(totallist[count]), True, STATUS_COLOR)
        # fill the screen and display the image and text
        game_screen.fill(BACK_COLOR)
        game_screen.blit(img, (272, 172))
        game_screen.blit(status_text, (0, 0))
        game_screen.blit(info_text, (0, 30))
        game_screen.blit(directory_text, (0, 60))
        game_screen.blit(img_text, (0, 580))
        # update the display and tick the clock
        pygame.display.flip()
        clock.tick(30)
    # quit the game
    pygame.quit()


if __name__ == "__main__":
    main()
