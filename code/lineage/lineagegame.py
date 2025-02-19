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
    game_init_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)
    pygame.display.update()
    game_init_clock = pygame.time.Clock()
    game_init_font = pygame.font.SysFont(None, 20)
    return game_init_window, game_init_clock, game_init_font


def text_screen(text_screen_text,
                text_screen_color,
                text_screen_x,
                text_screen_y,
                text_screen_font,
                text_screen_gameWindow):
    ''' display text on screen '''
    screen_text = text_screen_font.render(text_screen_text,
                                          True,
                                          text_screen_color)
    text_screen_gameWindow.blit(screen_text,
                                [text_screen_x, text_screen_y])


def lineage_game_loop(empire):
    ''' This is the main lineage game loop '''
    lineage_fed = fed(empire.currentPopulation(), empire.currentFood())
    lineage_birth = population_birth(empire.currentPopulation())
    lineage_death = population_decline(empire.currentPopulation())
    production_factor = production(empire.currentPopulation() - (lineage_death + lineage_birth))
    new_pop = empire.currentPopulation() + lineage_birth - lineage_death
    new_food = lineage_fed[2] + production_factor
    empire.updatePopulation(new_pop)
    empire.updateFood(new_food)
    return empire


def game_loop(gameitems):
    ''' main game loop '''
    game_window, clock, font = gameitems
    exit_game = False
    game_over = False
    year = 1
    # pop = 1000
    # food = 0
    clan = Empire()
    tribe = Empire()
    current_window = World()
    current_window.updateName("Earth")
    clan.updateName("Jackman Clan")
    tribe.updateName("McEoin Tribe")
    while not exit_game:
        if game_over:
            game_window.fill(WHITE)
            text_screen("Game Over! Press Enter To Continue",
                        RED,
                        100,
                        250,
                        font,
                        game_window)
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
            game_window.fill(WHITE)
            text_screen(f"Lineage Test # {VERSION}",
                        RED,
                        5,
                        5,
                        font,
                        game_window)
            text_screen("Lineage Data :",
                        BLACK,
                        5,
                        25,
                        font,
                        game_window)
            pygame.draw.line(game_window,
                             RED,
                             (0, 20),
                             (SCREEN_WIDTH, 20),
                             1)
            text_screen(f"World Information : Year - [{year}] : name: [{current_window.name}] ",
                        BLACK,
                        5,
                        40,
                        font, game_window)
            text_screen(f"Empire Information : name: [{clan}] pop - [{clan.currentPopulation():,}] food = [{clan.currentFood()}] ", NAVY, 5, 60, font, game_window)
            text_screen(f"Empire Information : name: [{tribe}] pop - [{tribe.currentPopulation():,}] food = [{tribe.currentFood()}] ", NAVY, 5, 80, font, game_window)
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
