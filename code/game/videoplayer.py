'''
    videoplayer example
'''
import pygame
import cv2

video = cv2.VideoCapture("Y:/pyproject/resources/clock.mp4")
success, video_image = video.read()
fps = video.get(cv2.CAP_PROP_FPS)
size = width, height = 800, 600
window = pygame.display.set_mode(size)
clock = pygame.time.Clock()

RUN = success
while RUN:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    success, video_image = video.read()
    if success:
        video_surf = pygame.image.frombuffer(
            video_image.tobytes(), video_image.shape[1::-1], "BGR")
        video_surf = pygame.transform.scale(video_surf, size)
    else:
        RUN = False
    window.blit(video_surf, (0, 0))
    pygame.display.flip()

pygame.quit()
