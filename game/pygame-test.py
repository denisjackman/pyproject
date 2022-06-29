# https://stackoverflow.com/questions/18067219/pygame-image-screen-fill
import pygame
pygame.init()
img = pygame.image.load("oreg.PNG")
white = (255, 255, 255)
w = 843
h = 798

screen = pygame.display.set_mode((w, h))
screen.fill((white))

screen.fill((white))
screen.blit(img, (0, 0))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
