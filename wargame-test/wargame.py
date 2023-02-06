''''
    This is a framework test for a wargame project.
    It is not intended to be a complete game, but rather a test of the framework.
'''
import pygame


WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)

def main():
    '''Main function'''
    # Initialise pygame
    pygame.init()
    pygame.font.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame_icon = pygame.image.load('y:/Resources/jackmanimation.png')
    caption = "Wargame Test"
    pygame.display.set_caption(f"{caption}")
    pygame.display.set_icon(pygame_icon)

    # Main Game loop
    run = True
    while run:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        window.fill((WHITE))
        pygame.display.update()

    # finish the game and quit
    pygame.quit()

if __name__ == "__main__":
    main()