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
WIDTH = 930
HEIGHT = 759
WHITE = (0, 0, 0)

def main():
    ''' main routine '''
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PyGame Template")
    pygame_icon = pygame.image.load('icon.png').convert()
    background = pygame.image.load("y:/tower-defense/tim-tower/game_assets/background.png").convert()
    clicks = []
    pygame.display.set_icon(pygame_icon)
    done = False
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicks.append(pos)
        window.fill(WHITE)
        window.blit(background, (0, 0))
        for item in clicks:
            pygame.draw.circle(window, (255, 0, 0), item, 5, 0)
        pygame.display.update()
        clock.tick(60)
    print(clicks)
if __name__ == '__main__':
    main()
