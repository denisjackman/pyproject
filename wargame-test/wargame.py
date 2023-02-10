''''
    This is a framework test for a wargame project.
    It is not intended to be a complete game, but rather a test of the framework.
'''
from pathlib import Path
import json
import pygame

WIDTH = 1200
HEIGHT = 900

GAME_WIDTH = 800
GAME_HEIGHT = 640
GAME_WINDOW_X = 10
GAME_WINDOW_Y = 250

TITLE_WIDTH = 800
TITLE_HEIGHT = 230 
TITLE_WINDOW_X = 10
TITLE_WINDOW_Y = 10

MENU_WIDTH = 370
MENU_HEIGHT = 880
MENU_WINDOW_X = 820
MENU_WINDOW_Y = 10

GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BROWN = (165, 42, 42)

FILEPATH = Path(__file__).parent
FONTDATA = "/data/Fontdata.json"

def main():
    '''Main function'''
    # Initialise pygame
    pygame.init()
    pygame.font.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame_icon = pygame.image.load('y:/Resources/jackmanimation.png')
    caption = "Wargame Test"
    pygame.display.set_caption(f"{caption}")
    pygame.display.set_icon(pygame_icon)
    game_window = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
    title_window = pygame.Surface((TITLE_WIDTH, TITLE_HEIGHT))
    menu_window = pygame.Surface((MENU_WIDTH, MENU_HEIGHT))
    listfonts= pygame.font.get_fonts()

    gamefont = pygame.font.SysFont('Arial', 24)
    gametext = gamefont.render('Game data is here', True, WHITE, BLACK)
    gametext_rect = gametext.get_rect()
    gametextwidth = gametext_rect.width
    gametextheight = gametext_rect.height
    
    titlefont = pygame.font.SysFont('footlight', 24)
    titletext = titlefont.render('Title information is here', True, BLACK, GRAY)
    titletext_rect = titletext.get_rect()
    titletextwidth = titletext_rect.width

    menufont = pygame.font.SysFont('couriernew', 30)
    menutext = menufont.render('Menu Items', True, WHITE, BROWN)
    menutext_rect = menutext.get_rect()
    menutextwidth = menutext_rect.width

    infofont = pygame.font.SysFont('couriernew', 20)
    # Main Game loop
    run = True
    info = "Mouse not pressed"
    while run:
        mousepos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                info = f"Mouse pressed at  x:{mousepos[0]} y:{mousepos[1]}"
            elif event.type == pygame.MOUSEBUTTONUP:
                info = f"Mouse released at  x:{mousepos[0]} y:{mousepos[1]}"
        
        infotext = infofont.render(info, True, WHITE, BROWN)
        mousetext = infofont.render(f"Mouse at x:{mousepos[0]} y:{mousepos[1]}", True, WHITE, BROWN)

        clock.tick(100)
        window.fill((WHITE))
        game_window.fill((BLACK))
        title_window.fill((GRAY))
        menu_window.fill((BROWN))

        game_window.blit(gametext, (GAME_WIDTH//2-gametextwidth//2, GAME_HEIGHT//2-gametextheight//2))
        title_window.blit(titletext, (TITLE_WIDTH//2-titletextwidth//2, 10))
        menu_window.blit(menutext, (MENU_WIDTH//2-menutextwidth//2, 10))
        menu_window.blit(infotext, (10, 50))
        menu_window.blit(mousetext, (10, 70))

        window.blit(game_window, (GAME_WINDOW_X, GAME_WINDOW_Y))
        window.blit(title_window, (TITLE_WINDOW_X, TITLE_WINDOW_Y))
        window.blit(menu_window, (MENU_WINDOW_X, MENU_WINDOW_Y))
        
        pygame.display.update()

    # finish the game and quit
    pygame.quit()
    with open(f"{FILEPATH}{FONTDATA}", "w", encoding='utf8') as file:
        json.dump({"pygame_fonts": listfonts,},
                  file,
                  indent=4,
                  ensure_ascii=False)

if __name__ == "__main__":
    main()
