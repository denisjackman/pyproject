'''
    another new game implementation
'''
import pygame


def MainGame():
    '''
        main game routine
    '''
    screen = pygame.display.set_mode((640, 480))
    # set screen size of pygame window
    background = pygame.Surface(screen.get_size())
    # Create empty pygame surface
    background.fill((255, 255, 255))
    # Fill the background white color (red,green,blue)
    background = background.convert()
    # Convert Surface to make blitting faster
    screen.blit(background, (0, 0))
    mainloop = True
    while mainloop:
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


def main():
    '''
        main function
    '''
    pygame.init()
    MainGame()
    pygame.quit()                                   # idle-friendly quit method


if __name__ == '__main__':
    main()
