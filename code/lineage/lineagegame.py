''' new snake game '''
import os
import sys
import pygame
# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))

from jackmanimation.gameitems.colours import WHITE
from jackmanimation.gameitems.colours import RED
from jackmanimation.gameitems.colours import BLACK


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
CAPTION = "Lineage"
FPS = 60
VERSION = "v1.00.00.a"

def game_init():
    ''' initialize the game '''
    pygame.init()
    giWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)
    pygame.display.update()
    giclock = pygame.time.Clock()
    gifont = pygame.font.SysFont(None, 20)
    return giWindow, giclock, gifont

def text_screen(text, color, x, y, tfont, tgameWindow):
    ''' display text on screen '''
    screen_text = tfont.render(text, True, color)
    tgameWindow.blit(screen_text, [x,y])

def game_loop(gameitems):
    ''' main game loop '''
    gameWindow, clock, font = gameitems
    exit_game = False
    game_over = False

    while not exit_game:
        if game_over:
            gameWindow.fill(WHITE)
            text_screen("Game Over! Press Enter To Continue", RED, 100, 250, font, gameWindow)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop(gameitems)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

            gameWindow.fill(WHITE)
            text_screen(f"Lineage Test # {VERSION}", RED, 5, 5,font, gameWindow)
            text_screen("Lineage Data :", BLACK, 5, 25, font, gameWindow)
            pygame.draw.line(gameWindow, RED, (0, 20), (SCREEN_WIDTH, 20), 1)

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()

def main():
    ''' This is the main routine for the program '''
    item = game_init()
    game_loop(item)

if __name__ == "__main__":
    main()
