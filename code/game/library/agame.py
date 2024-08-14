'''
    a game template
'''
import pygame


def main():
    ''' main function '''
    pygame.init()
    # initialize pygame
    screen = pygame.display.set_mode((640, 480))
    # set screensize of pygame window
    background = pygame.Surface(screen.get_size())
    # create empty pygame surface
    background.fill((255, 255, 255))
    # fill the background white color (red,green,blue)
    background = background.convert()
    # convert Surface object to make blitting faster
    screen.blit(background, (0, 0))
    # draw the background on screen
    clock = pygame.time.Clock()
    # create a pygame clock object
    MAINLOOP = True
    FPS = 30
    # desired framerate in frames per second. try out other values !
    PLAYTIME = 0.0
    # how many seconds the "game" is played
    while MAINLOOP:
        milliseconds = clock.tick(FPS)
        # do not go faster than this framerate
        PLAYTIME += milliseconds / 1000.0
        # add seconds to PLAYTIME
        print(f'{milliseconds} milliseconds passed since last frame')
        # brackets for python3.x
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MAINLOOP = False
                # pygame window closed by user
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    MAINLOOP = False
                    # user pressed ESC
                    # # print the framerate and
                    # PLAYTIME into the pygame window title
        pygame.display.set_caption(f'frame rate: {clock.get_fps()} frames per second, PLAYTIME: {PLAYTIME} seconds')
        pygame.display.flip()
        # flip the screen like in a flip book
    print(f"This 'game' was played for {PLAYTIME} seconds")
    pygame.quit()
    # idle-friendly quit method


if __name__ == '__main__':
    main()
