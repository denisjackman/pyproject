''''
    This is a framework test for a wargame project.
    It is not intended to be a complete game,
    but rather a test of the framework.
'''
import json
import pygame
# pylint: disable=too-many-locals
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

FONTDATA = "Z:/Resources/development/data/Fontdata.json"
TILE_WIDTH = 64
TILE_HEIGHT = 64

GRASS_TILE_01 = pygame.image.load('Z:/Resources/development/game-assets/tiles/grass001.png')
GRASS_TILE_02 = pygame.image.load('Z:/Resources/development/game-assets/tiles/grass002.png')
GRASS_TILE_03 = pygame.image.load('Z:/Resources/development/game-assets/tiles/grass003.png')
DIRT_TILE_01 = pygame.image.load('Z:/Resources/development/game-assets/tiles/dirt001.png')
DIRT_TILE_02 = pygame.image.load('Z:/Resources/development/game-assets/tiles/dirt002.png')
SAND_TILE_01 = pygame.image.load('Z:/Resources/development/game-assets/tiles/sand001.png')
SAND_TILE_02 = pygame.image.load('Z:/Resources/development/game-assets/tiles/sand002.png')
STONE_TILE_01 = pygame.image.load('Z:/Resources/development/game-assets/tiles/stone001.png')
STONE_TILE_02 = pygame.image.load('Z:/Resources/development/game-assets/tiles/stone002.png')
STONE_TILE_03 = pygame.image.load('Z:/Resources/development/game-assets/tiles/stone003.png')
WATER_TILE_01 = pygame.image.load('Z:/Resources/development/game-assets/tiles/water001.png')
WATER_TILE_02 = pygame.image.load('Z:/Resources/development/game-assets/tiles/water002.png')
WATER_TILE_03 = pygame.image.load('Z:/Resources/development/game-assets/tiles/water003.png')
WATER_TILE_04 = pygame.image.load('Z:/Resources/development/game-assets/tiles/water004.png')
WATER_BOTTOM = pygame.image.load('Z:/Resources/development/game-assets/tiles/water-bottom.png')
WATER_BOTTOM_RIGHT = pygame.image.load('Z:/Resources/development/game-assets/tiles/water-bottomright.png')
WATER_BOTTOM_LEFT = pygame.image.load('Z:/Resources/development/game-assets/tiles/water-bottomleft.png')
WATER_LEFT = pygame.image.load('Z:/Resources/development/game-assets/tiles/water-left.png')
WATER_RIGHT = pygame.image.load('Z:/Resources/development/game-assets/tiles/water-right.png')
WATER_TOP = pygame.image.load('Z:/Resources/development/game-assets/tiles/water-top.png')
WATER_TOP_LEFT = pygame.image.load('Z:/Resources/development/game-assets/tiles/water-topleft.png')
WATER_TOP_RIGHT = pygame.image.load('Z:/Resources/development/game-assets/tiles/water-topright.png')

TILES = []
TILES.append(pygame.transform.scale(GRASS_TILE_01, (TILE_WIDTH, TILE_HEIGHT)))  # 0
TILES.append(pygame.transform.scale(GRASS_TILE_02, (TILE_WIDTH, TILE_HEIGHT)))  # 1
TILES.append(pygame.transform.scale(GRASS_TILE_03, (TILE_WIDTH, TILE_HEIGHT)))  # 2
TILES.append(pygame.transform.scale(DIRT_TILE_01, (TILE_WIDTH, TILE_HEIGHT)))  # 3
TILES.append(pygame.transform.scale(DIRT_TILE_02, (TILE_WIDTH, TILE_HEIGHT)))  # 4
TILES.append(pygame.transform.scale(SAND_TILE_01, (TILE_WIDTH, TILE_HEIGHT)))  # 5
TILES.append(pygame.transform.scale(SAND_TILE_02, (TILE_WIDTH, TILE_HEIGHT)))  # 6
TILES.append(pygame.transform.scale(STONE_TILE_01, (TILE_WIDTH, TILE_HEIGHT)))  # 7
TILES.append(pygame.transform.scale(STONE_TILE_02, (TILE_WIDTH, TILE_HEIGHT)))  # 8
TILES.append(pygame.transform.scale(STONE_TILE_03, (TILE_WIDTH, TILE_HEIGHT)))  # 9
TILES.append(pygame.transform.scale(WATER_TILE_01, (TILE_WIDTH, TILE_HEIGHT)))  # 10
TILES.append(pygame.transform.scale(WATER_TILE_02, (TILE_WIDTH, TILE_HEIGHT)))  # 11
TILES.append(pygame.transform.scale(WATER_TILE_03, (TILE_WIDTH, TILE_HEIGHT)))  # 12
TILES.append(pygame.transform.scale(WATER_TILE_04, (TILE_WIDTH, TILE_HEIGHT)))  # 13
TILES.append(pygame.transform.scale(WATER_BOTTOM, (TILE_WIDTH, TILE_HEIGHT)))  # 14
TILES.append(pygame.transform.scale(WATER_BOTTOM_RIGHT, (TILE_WIDTH, TILE_HEIGHT)))  # 15
TILES.append(pygame.transform.scale(WATER_BOTTOM_LEFT, (TILE_WIDTH, TILE_HEIGHT)))  # 16
TILES.append(pygame.transform.scale(WATER_LEFT, (TILE_WIDTH, TILE_HEIGHT)))  # 17
TILES.append(pygame.transform.scale(WATER_RIGHT, (TILE_WIDTH, TILE_HEIGHT)))  # 18
TILES.append(pygame.transform.scale(WATER_TOP, (TILE_WIDTH, TILE_HEIGHT)))  # 19
TILES.append(pygame.transform.scale(WATER_TOP_LEFT, (TILE_WIDTH, TILE_HEIGHT)))  # 20
TILES.append(pygame.transform.scale(WATER_TOP_RIGHT, (TILE_WIDTH, TILE_HEIGHT)))  # 21

GAMEMAP = [[0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0],
           [0, 1, 2, 0, 2, 1,
            0, 2, 1, 0, 2, 1],
           [0, 8, 9, 8, 9, 8,
            9, 8, 9, 8, 9, 0],
           [0, 3, 4, 3, 4, 3,
            4, 3, 4, 3, 4, 0],
           [0, 20, 19, 19, 19,
            19, 19, 19, 19, 19, 21, 0],
           [0, 17, 10, 11, 10,
            11, 10, 11, 10, 11, 18, 0],
           [0, 16, 14, 14, 14,
            14, 14, 14, 14, 14, 15, 0],
           [0, 5, 6, 5, 6, 5,
            6, 5, 6, 5, 6, 0],
           [0, 2, 1, 0, 2, 0,
            1, 2, 1, 1, 2, 0],
           [0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0]]


def build_map(width, height):
    '''Build the map'''
    returnmap = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(0)
        returnmap.append(row)
    return returnmap


def main():
    '''Main function'''
    # Initialise pygame
    pygame.init()
    pygame.font.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame_icon = pygame.image.load('Z:/Resources/jackmanimation.png')
    caption = "Wargame Test"
    pygame.display.set_caption(f"{caption}")
    pygame.display.set_icon(pygame_icon)

    game_window = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
    title_window = pygame.Surface((TITLE_WIDTH, TITLE_HEIGHT))
    menu_window = pygame.Surface((MENU_WIDTH, MENU_HEIGHT))

    listfonts = pygame.font.get_fonts()

    titlefont = pygame.font.SysFont('footlight', 24)
    titletext = titlefont.render('Title information is here',
                                 True,
                                 BLACK, GRAY)
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
        mousetext = infofont.render(f"Mouse at x:{mousepos[0]} y:{mousepos[1]}",
                                    True, WHITE, BROWN)
        maptext = infofont.render(f"Map is {len(GAMEMAP[0])}:Wide x {len(GAMEMAP)}:High", True, WHITE, BROWN)
        spritetext = infofont.render(f"Sprite is {TILES[0].get_width()}:Wide x {TILES[0].get_height()}:High", True, WHITE, BROWN)
        tiletext = infofont.render(f"map is {len(GAMEMAP[0])}:Wide x {len(GAMEMAP)}:High", True, WHITE, BROWN)

        clock.tick(100)
        window.fill((WHITE))
        game_window.fill((BLACK))
        title_window.fill((GRAY))
        menu_window.fill((BROWN))

        for y in range(len(GAMEMAP)):
            for x in range(len(GAMEMAP[y])):
                game_window.blit(TILES[GAMEMAP[y][x]],
                                 (x*TILES[0].get_width(),
                                  y*TILES[0].get_height()))

        title_window.blit(titletext, (TITLE_WIDTH//2-titletextwidth//2, 10))

        menu_window.blit(menutext, (MENU_WIDTH//2-menutextwidth//2, 10))
        menu_window.blit(infotext, (10, 50))
        menu_window.blit(mousetext, (10, 70))
        menu_window.blit(maptext, (10, 90))
        menu_window.blit(spritetext, (10, 110))
        menu_window.blit(tiletext, (10, 130))

        window.blit(game_window, (GAME_WINDOW_X, GAME_WINDOW_Y))
        window.blit(title_window, (TITLE_WINDOW_X, TITLE_WINDOW_Y))
        window.blit(menu_window, (MENU_WINDOW_X, MENU_WINDOW_Y))

        pygame.display.update()

    # finish the game and quit
    pygame.quit()
    with open(f"{FONTDATA}",
              "w",
              encoding='utf-8-sig') as file:
        json.dump({"pygame_fonts": listfonts},
                  file,
                  indent=4,
                  ensure_ascii=False)


if __name__ == "__main__":
    main()
