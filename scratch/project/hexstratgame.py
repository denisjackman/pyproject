'''

    A test for a pygame

    references:
    Hex Grids   : https://www.redblobgames.com/grids/hexagons/
    Hex Sprites : https://opengameart.org/content/hexagon-pack-310x
    Hex Map Tool: https://www.youtube.com/watch?v=wZXW_nzJotc

'''
from random import randint
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

WIDTH = 1200
HEIGHT = 900
SCREEN_SIZE = (WIDTH, HEIGHT)

CAPTION = 'Hex Strat Game'

ICON_FILE = 'y:/Resources/Logo-001.jpg'
#HEX_SHEET = 'y:/pyproject/scratch/project/hexagonAll_sheet.png'
HEX_TILE = 'y:/pyproject/scratch/project/grass_01.png'

SPRITE_X = 0
SPRITE_Y = 0
START_POSX = 0
START_POSY = 0

SPRITE_WIDTH = 120
SPRITE_HEIGHT = 140
SEPARATION = 2
TILEWIDTH = 9
TILEHEIGHT = 8

VERT = 3/4 * (SPRITE_HEIGHT + SEPARATION)
WIDTH = math.sqrt(3) * (SPRITE_HEIGHT + SEPARATION)/2
pygame.init()

GAME_SCREEN = pygame.display.set_mode(SCREEN_SIZE)
GAME_CLOCK = pygame.time.Clock()

sprite_size = (SPRITE_WIDTH, SPRITE_HEIGHT)
grasstile = pygame.image.load(HEX_TILE).convert_alpha()
grasstile = pygame.transform.scale(grasstile, sprite_size)

def game_initialise():
    '''Initialises the game'''
    icon = pygame.image.load(ICON_FILE)
    pygame.display.set_caption(CAPTION)
    pygame.display.set_icon(icon)

def dice(sides=6, rolls=1):
    '''
        Rolls a dice which has 'sides' sides (default is six (6))
        for 'rolls' number of times (default is one (1))
    '''
    result = 0
    item = 0
    while item in range(rolls):
        result = result + randint(1, sides)
        item += 1
    return result

def hexmap_type():
    '''Returns a random hexmap tile type'''
    result = ''
    roll = dice(20)
    typeroll = dice()
    if roll == 1:
        result = "City"
        if typeroll == 1:
            result = f"{result} : Capital City"
        elif typeroll == 2:
            result = f"{result} : Free City"
        elif typeroll == 3:
            result = f"{result} : Ruined City"
        elif typeroll == 4:
            result = f"{result} : Towering City"
        elif typeroll == 5:
            result = f"{result} : Magical City"
        else:
            result = f"{result} : Besiged City"
    elif roll == 2:
        result = "Castle/Fort"
        if typeroll == 1:
            result = f"{result} : Guarded Fort"
        elif typeroll == 2:
            result = f"{result} : Deserted Fort"
        elif typeroll == 3:
            result = f"{result} : Lord's Castle"
        elif typeroll == 4:
            result = f"{result} : Royal Keep"
        elif typeroll == 5:
            result = f"{result} : Military Keep"
        else:
            result = f"{result} : Ruined Fort"
    elif roll == 3:
        result = "Town"
        if typeroll == 1:
            result = f"{result} : Bustling Town"
        elif typeroll == 2:
            result = f"{result} : Shanty Town"
        elif typeroll == 3:
            result = f"{result} : Plagued Town"
        elif typeroll == 4:
            result = f"{result} : Stone Town"
        elif typeroll == 5:
            result = f"{result} : Wooden Town"
        else:
            result = f"{result} : Store Fronts"
    elif roll == 4:
        result = "Village"
        if typeroll == 1:
            result = f"{result} : Farm Village"
        elif typeroll == 2:
            result = f"{result} : Tribal Village"
        elif typeroll == 3:
            result = f"{result} : Bandit Camp"
        elif typeroll == 4:
            result = f"{result} : Hunter's Camp"
        elif typeroll == 5:
            result = f"{result} : Empty Village"
        else:
            result = f"{result} : Apothecary"
    elif roll == 5:
        result = "Forest / Woodland"
        if typeroll == 1:
            result = f"{result} : Dense Forest"
        elif typeroll == 2:
            result = f"{result} : Dying Forest"
        elif typeroll == 3:
            result = f"{result} : Sparse Forest"
        elif typeroll == 4:
            result = f"{result} : Cursed Forest"
        elif typeroll == 5:
            result = f"{result} : Woodland"
        else:
            result = f"{result} : Magical Woods"
    elif roll == 6:
        result = "Mountains"
        if typeroll == 1:
            result = f"{result} : Jagged Peaks"
        elif typeroll == 2:
            result = f"{result} : Cold Mountains"
        elif typeroll == 3:
            result = f"{result} : Shadowy Range"
        elif typeroll == 4:
            result = f"{result} : Magical Peak"
        elif typeroll == 5:
            result = f"{result} : Snowy Bluffs"
        else:
            result = f"{result} : Mountains"
    elif roll == 7:
        result = "Grassland"
        if typeroll == 1:
            result = f"{result} : Grassland"
        elif typeroll == 2:
            result = f"{result} : Meadows"
        elif typeroll == 3:
            result = f"{result} : Fields"
        elif typeroll == 4:
            result = f"{result} : Flooded Plains"
        elif typeroll == 5:
            result = f"{result} : Flatland"
        else:
            result = f"{result} : Savannah"
    elif roll == 8:
        result = "Hills / Heath"
        if typeroll == 1:
            result = f"{result} : Hills"
        elif typeroll == 2:
            result = f"{result} : Heath"
        elif typeroll == 3:
            result = f"{result} : Outcropping"
        elif typeroll == 4:
            result = f"{result} : Burial Mounds"
        elif typeroll == 5:
            result = f"{result} : Wet Moors"
        else:
            result = f"{result} : Highland"
    elif roll == 9:
        result = "River"
        if typeroll == 1:
            result = f"{result} : Rushing River"
        elif typeroll == 2:
            result = f"{result} : Canal"
        elif typeroll == 3:
            result = f"{result} : Streams"
        elif typeroll == 4:
            result = f"{result} : Magical River"
        elif typeroll == 5:
            result = f"{result} : Slow River"
        else:
            result = f"{result} : Posioned River"
    elif roll == 10:
        result = "Desert"
        if typeroll == 1:
            result = f"{result} : Hot Desert"
        elif typeroll == 2:
            result = f"{result} : Dry Steppe"
        elif typeroll == 3:
            result = f"{result} : Wasteland"
        elif typeroll == 4:
            result = f"{result} : Cacti Forest"
        elif typeroll == 5:
            result = f"{result} : Cold Desert"
        else:
            result = f"{result} : Deadlands"
    elif roll == 11:
        result = "Water / Lake / Sea"
        if typeroll == 1:
            result = f"{result} : Sea"
        elif typeroll == 2:
            result = f"{result} : Ocean"
        elif typeroll == 3:
            result = f"{result} : Lake"
        elif typeroll == 4:
            result = f"{result} : Reservoir"
        elif typeroll == 5:
            result = f"{result} : Magical Pools"
        else:
            result = f"{result} : Flooded Land"
    elif roll == 12:
        result = "Swamp / Marshland"
        if typeroll == 1:
            result = f"{result} : Swampland"
        elif typeroll == 2:
            result = f"{result} : Putrid Fen"
        elif typeroll == 3:
            result = f"{result} : Sinking Bog"
        elif typeroll == 4:
            result = f"{result} : Cursed Mire"
        elif typeroll == 5:
            result = f"{result} : Muddy Land"
        else:
            result = f"{result} : Marshland"
    elif roll == 13:
        result = "Tundra / Frozen Waste"
        if typeroll == 1:
            result = f"{result} : Snowy Flats"
        elif typeroll == 2:
            result = f"{result} : Blizzards"
        elif typeroll == 3:
            result = f"{result} : Tundra"
        elif typeroll == 4:
            result = f"{result} : Frozen Waste"
        elif typeroll == 5:
            result = f"{result} : Ice"
        else:
            result = f"{result} : Artic Expanse"
    elif roll == 14:
        result = "Jungle"
        if typeroll == 1:
            result = f"{result} : Jungle"
        elif typeroll == 2:
            result = f"{result} : Rainforest"
        elif typeroll == 3:
            result = f"{result} : Tropical Land"
        elif typeroll == 4:
            result = f"{result} : Cursed Jungle"
        elif typeroll == 5:
            result = f"{result} : Bushland"
        else:
            result = f"{result} : Tangled Jungle"
    elif roll == 15:
        result = "Volcano"
        if typeroll == 1:
            result = f"{result} : Volcano"
        elif typeroll == 2:
            result = f"{result} : Planar Break"
        elif typeroll == 3:
            result = f"{result} : Mage's Peak"
        elif typeroll == 4:
            result = f"{result} : Magical Source"
        elif typeroll == 5:
            result = f"{result} : Volcanic Land"
        else:
            result = f"{result} : Gas Clouds"
    elif roll == 16:
        result = "Cave / Dungeon"
        if typeroll == 1:
            result = f"{result} : Cave"
        elif typeroll == 2:
            result = f"{result} : Grotto"
        elif typeroll == 3:
            result = f"{result} : Hill Home"
        elif typeroll == 4:
            result = f"{result} : Dugout Camp"
        elif typeroll == 5:
            result = f"{result} : Tomb"
        else:
            result = f"{result} : Passageway"
    elif roll == 17:
        result = "Fissure / Canyon"
        if typeroll == 1:
            result = f"{result} : Fissure"
        elif typeroll == 2:
            result = f"{result} : Dry Canyon"
        elif typeroll == 3:
            result = f"{result} : River Gorge"
        elif typeroll == 4:
            result = f"{result} : Icy Crevasse"
        elif typeroll == 5:
            result = f"{result} : World Rift"
        else:
            result = f"{result} : Valley"
    elif roll == 18:
        result = "Fungal Forest"
        if typeroll == 1:
            result = f"{result} : Fungal Forest"
        elif typeroll == 2:
            result = f"{result} : Faeland"
        elif typeroll == 3:
            result = f"{result} : Rotten Place"
        elif typeroll == 4:
            result = f"{result} : Fungal Fields"
        elif typeroll == 5:
            result = f"{result} : Sporeland"
        else:
            result = f"{result} : Toadstool Town"
    elif roll == 19:
        result = "Crystal Plains"
        if typeroll == 1:
            result = f"{result} : Crystal Plains"
        elif typeroll == 2:
            result = f"{result} : Crystal Forest"
        elif typeroll == 3:
            result = f"{result} : Shard Tower"
        elif typeroll == 4:
            result = f"{result} : Magical Plane"
        elif typeroll == 5:
            result = f"{result} : Gemstone Mine"
        else:
            result = f"{result} : Crystal Gate"
    else:
        result = "Map Marker / Unknown Location"
        if typeroll == 1:
            result = f"{result} : Dungeon"
        elif typeroll == 2:
            result = f"{result} : Treasure"
        elif typeroll == 3:
            result = f"{result} : Artefact"
        elif typeroll == 4:
            result = f"{result} : MPC Location"
        elif typeroll == 5:
            result = f"{result} : Guild Base"
        else:
            result = f"{result} : Hidden Temple"
    return result

def check_game_status():
    '''
        this checks the status of the game and return True is it should keep
        running False is not.
        There are no parameters to be passed and it returns a boolean as a
        response.
    '''
    game_status = True
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_status = False
        elif event.type == QUIT:
            game_status = False
    return game_status

def draw_hexagon(tile_x, tile_y, tile_image):
    ''' draw a hexagon at the given x,y coordinates using the given image'''
    GAME_SCREEN.blit(tile_image, (tile_x, tile_y))

def draw_map():
    ''' draw the map '''
    screenx = 0
    screeny = 0
    ty = 0
    for ty in range(1, TILEHEIGHT + 1):
        if ty % 2 == 0:
            screenx = (SPRITE_WIDTH + SEPARATION)/2
        else:
            screenx = 0
        for _ in range(1, TILEWIDTH + 1):
            draw_hexagon(screenx, screeny, grasstile)
            screenx = screenx + SPRITE_WIDTH + SEPARATION
        screeny += VERT

def game_housekeeping():
    ''' housekeeping for the game '''
    mouse_x,mouse_y = pygame.mouse.get_pos()
    hx = round(mouse_x / SPRITE_WIDTH)
    hy = round(mouse_y / SPRITE_HEIGHT)
    newcaption = f'Hex Strat Game - ( x: {mouse_x} y: {mouse_y} ) ( hx: {hx} hy: {hy} )'
    pygame.display.set_caption(newcaption)

def game_main():
    '''
        main routine
    '''
    run_game = True

    while run_game:
        run_game = check_game_status()
        GAME_SCREEN.fill(WHITE)
        draw_map()
        game_housekeeping()
        pygame.display.flip()
        GAME_CLOCK.tick(30)
    pygame.quit()

if __name__ == '__main__':
    game_initialise()
    game_main()
