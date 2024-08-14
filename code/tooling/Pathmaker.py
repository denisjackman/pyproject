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
            exit the program and a file will be created
            in the data folder with the path data.
            The path data is a list of tuples.
            the path data is stored in a json file.
            the path data is stored in a dictionary with the key "npc_path"
            The path data printed on the console in a list of tuples.
'''
from pathlib import Path
import json
import sys
import getopt
import pygame

WIDTH = 1350
HEIGHT = 700
MAP = "Z:/tower-defense/tim-tower/game_assets/td-tilesets1-2/tower-defense-game-tilesets/PNG/game_background_2/game_background_2.png"

PROGRAM_NAME = sys.argv[0][2:].replace(".py", "")
STANDARD_COMMANDS = f'{PROGRAM_NAME} -v <True/False> -d <True/False> -m MAPNAME -mw MAPWIDTH -mh MAPHEIGHT '
LONG_STANDARD_COMMANDS = f'{PROGRAM_NAME} --verbose <True/False> --debug <True/False> --map MAPNAME --mapwidth MAPWIDTH --mapheight MAPHEIGHT '
COMMANDS = "hvdm:mw:mh:"
LONG_COMMANDS = ["help", "verbose", "debug", "map=", "mapwidth=", "mapheight="]
FILEPATH = Path(__file__).parent

ICON_FILE = 'Z:/Resources/jackmanimation.png'
GAMEDATA = "Z:/Resources/devlopement/work/data/Gamedata.json"
CAPTION = f"Jackmanimation [{PROGRAM_NAME}]"


def getargs():
    '''
        get the arguments from the command line
    '''
    argv = sys.argv[1:]
    verbosemode = False
    debugmode = False
    mymap = MAP
    mymapwidth = WIDTH
    mymapheight = HEIGHT

    try:
        command_line_optionss, args = getopt.getopt(argv, COMMANDS, LONG_COMMANDS)
    except getopt.GetoptError:
        print(f'The commands are : {STANDARD_COMMANDS}')
        sys.exit(2)
    for command_line_options, arg in command_line_optionss:
        if command_line_options in ('-h', "--help"):
            print(f'The commands are : {STANDARD_COMMANDS}')
            print(f'The long commands are : {LONG_STANDARD_COMMANDS}')
            sys.exit()
        elif command_line_options in ("-v", "--verbose"):
            verbosemode = True
        elif command_line_options in ("-d", "--debug"):
            debugmode = True
        elif command_line_options in ("-m", "--map"):
            mymap = arg
        elif command_line_options in ("-mw", "--mapwidth"):
            mymapwidth = arg
        elif command_line_options in ("-mh", "--mapheight"):
            mymapheight = arg
    return {"verbosemode": verbosemode,
            "debugmode": debugmode,
            "mymap": mymap,
            "mymapwidth": int(mymapwidth),
            "mymapheight": int(mymapheight)}


def main():
    ''' main routine '''
    pygame.init()
    mainargs = getargs()
    window = pygame.display.set_mode((mainargs["mymapwidth"], mainargs["mymapheight"]))
    pygame.display.set_caption(CAPTION)
    pygame_icon = pygame.image.load(ICON_FILE)
    background = pygame.image.load(mainargs["mymap"]).convert()
    background = pygame.transform.scale(background, (mainargs["mymapwidth"], mainargs["mymapheight"]))
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
    with open(f"{FILEPATH}{GAMEDATA}", "w", encoding='utf-8-sig') as file:
        json.dump({"npc_path": clicks},
                  file,
                  indent=4,
                  ensure_ascii=False)
    print(f"{clicks}")


if __name__ == '__main__':
    main()
