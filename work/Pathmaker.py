'''
    Name: Pathmaker.py
    Authored by: Jackmanimation
    Date: 2023-01-28
    Version: 1.0

    Notes:
            This is a pathmaker tool.
            Set the WIDTH and HEIGHT to the size of your map.
            Set the MAP to the path of your map.
            Run the program and click on the map to create a path.
            exit the program and a file will be created in the data folder with the path data.
            The path data is a list of tuples.
            the path data is stored in a json file.
            the path data is stored in a dictionary with the key "npc_path"
            The path data printed on the console in a list of tuples.
'''
from pathlib import Path
import json
import pygame

WIDTH = 930
HEIGHT = 759
MAP = "y:/tower-defense/tim-tower/game_assets/background.png"

FILEPATH = Path(__file__).parent
ICON_FILE = 'y:/Resources/images/Jack.png'
GAMEDATA = "/data/Gamedata.json"
CAPTION = "Jackmanimation PATHMAKER"

def main():
    ''' main routine '''
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(CAPTION)
    pygame_icon = pygame.image.load(ICON_FILE)
    background = pygame.image.load(MAP).convert()
    clicks = []
    pygame.display.set_icon(pygame_icon)
    done = False
    while not done:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicks.append(pos)
        window.blit(background, (0, 0))
        for item in clicks:
            pygame.draw.circle(window, (255, 0, 0), item, 5, 0)
        pygame.display.update()
    print(clicks)
    with open(f"{FILEPATH}{GAMEDATA}", "w", encoding='utf8') as file:
        json.dump({"npc_path": clicks,},
                  file,
                  indent=4,
                  ensure_ascii=False)

if __name__ == '__main__':
    main()
