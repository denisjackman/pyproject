'''
    nupygametest
'''
# Install libraries
# pip install pygame
import pygame


def main():
    '''
        main function
    '''
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    DONE = False
    IS_BLUE = True
    while not DONE:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                IS_BLUE = not IS_BLUE
            if event.type == pygame.QUIT:
                DONE = True
        if IS_BLUE:
            color = (0, 128, 255)
        else:
            color = (255, 100, 0)

        pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
        pygame.display.flip()


if __name__ == '__main__':
    main()
