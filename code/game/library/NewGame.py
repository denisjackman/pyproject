'''
    new game
'''
import pygame
from djgamemodule import colours as gc


def MainGame():
    '''
        Main Game routine
    '''
    screen = pygame.display.set_mode((640, 480))
    # set screen size of pygame window
    background = pygame.Surface(screen.get_size())
    # Create empty pygame surface
    colorlist = []
    for colour_name, color in gc.COLOURS_RGB_LIST.items():
        colorlist.append(color)
    loop = 0
    mainloop = True
    clock = pygame.time.Clock()
    while mainloop:
        background.fill(colorlist[loop])
        # Fill the background white color (red,green,blue)
        background = background.convert()
        # Convert Surface to make blitting faster
        screen.blit(background, (0, 0))
        loop += 1
        if loop >= len(colorlist):
            loop = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False
                # pygame window closed by user
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False
                    # user pressed ESC
                    # print the framerate and playtime
                    # into the pygame window title
        pygame.display.set_caption("NewGame")
        pygame.display.flip()
        # flip the screen like in a flip book
        clock.tick(30)


def main():
    '''
        main function
    '''
    # start of it all
    pygame.init()
    MainGame()
    pygame.quit()                                   # idle-friendly quit method


if __name__ == '__main__':
    main()
