'''
    This is a scratch python script
    links :
            Tutorial    : https://www.youtube.com/watch?v=JGxFPCkJzJM
            Source Code : https://github.com/hamletrpg/RPG-Battle-System/tree/master
            Assets      : https://drive.google.com/drive/folders/1XzR4oGCKbLeHuOP37tuKnxFTKCclLnhL
            Reference   : https://www.pygame.org/project-Simple+turn-based+strategy+game-2795-.html
'''
import pygame

pygame.init()
WIDTH = 400
HEIGHT = 500
WHITE = (0, 0, 0)

def main():
    ''' main routine '''
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PyGame Template")
    pygame_icon = pygame.image.load('icon.png')
    background = pygame.image.load("background.png").convert()

    pygame.display.set_icon(pygame_icon)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        window.fill(WHITE)
        window.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__':
    main()
