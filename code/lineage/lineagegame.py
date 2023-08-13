''' new snake game '''
import os
import sys
import pygame

from lineageclasses.empire import Empire
from lineageclasses.world import World

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))

from jackmanimation.gameitems.colours import WHITE
from jackmanimation.gameitems.colours import RED
from jackmanimation.gameitems.colours import BLACK
from jackmanimation.gameitems.colours import NAVY

from jackmanimation.lineage.lineage import fed
from jackmanimation.lineage.lineage import population_birth
from jackmanimation.lineage.lineage import population_decline
from jackmanimation.lineage.lineage import production


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

def lineage_game_loop(empire):
    ''' This is the main lineage game loop '''
    lgfed = fed(empire.currentPopulation(), empire.currentFood())
    ldbirth = population_birth(empire.currentPopulation())
    lddeath = population_decline(empire.currentPopulation())
    production_factor = production(empire.currentPopulation() - (lddeath + ldbirth))
    newpop = empire.currentPopulation() + ldbirth - lddeath
    newfood = lgfed[2] + production_factor
    empire.updatePopulation(newpop)
    empire.updateFood(newfood)
    return empire

def game_loop(gameitems):
    ''' main game loop '''
    gameWindow, clock, font = gameitems
    exit_game = False
    game_over = False
    year = 1
    pop = 1000
    food = 0
    clan = Empire()
    tribe = Empire()
    currentWorld = World()
    currentWorld.updateName("Earth")
    clan.updateName("Jackman Clan")
    tribe.updateName("McEoin Tribe")
    while not exit_game:
        if game_over:
            gameWindow.fill(WHITE)
            text_screen("Game Over! Press Enter To Continue", RED, 100, 250, font, gameWindow)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    year += 1
                    clan = lineage_game_loop(clan)
                    tribe = lineage_game_loop(tribe)
            gameWindow.fill(WHITE)
            text_screen(f"Lineage Test # {VERSION}", RED, 5, 5,font, gameWindow)
            text_screen("Lineage Data :", BLACK, 5, 25, font, gameWindow)
            pygame.draw.line(gameWindow, RED, (0, 20), (SCREEN_WIDTH, 20), 1)
            text_screen(f"World Information : Year - [{year}] : name: [{currentWorld.name}] ", BLACK, 5, 40, font, gameWindow)
            text_screen(f"Empire Information : name: [{clan}] pop - [{clan.currentPopulation():,}] food = [{clan.currentFood()}] ", NAVY, 5, 60, font, gameWindow)
            text_screen(f"Empire Information : name: [{tribe}] pop - [{tribe.currentPopulation():,}] food = [{tribe.currentFood()}] ", NAVY, 5, 80, font, gameWindow)
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
