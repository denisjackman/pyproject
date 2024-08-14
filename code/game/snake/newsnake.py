''' new snake game '''
import random
import sys
import pygame

pygame.init()
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

gameWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    ''' display text on screen '''
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(psWindow, color, snake_list, snake_size):
    ''' display snake on screen '''
    for x, y in snake_list:
        pygame.draw.rect(psWindow, color, [x, y, snake_size, snake_size])


def game_loop():
    ''' main game loop '''
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []

    fps = 60

    food_x = random.randint(20, SCREEN_WIDTH - 20)
    food_y = random.randint(60, SCREEN_HEIGHT - 60)

    score = 0
    init_velocity = 1
    snake_size = 30
    while not exit_game:
        if game_over:
            gameWindow.fill(WHITE)
            text_screen("Game Over! Press Enter To Continue",
                        RED,
                        100,
                        250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 1
                food_x = random.randint(20, SCREEN_WIDTH - 20)
                food_y = random.randint(60, SCREEN_HEIGHT - 60)
                snake_size += 5
            gameWindow.fill(WHITE)
            text_screen("Score: " + str(score * 10),
                        RED,
                        5,
                        5)
            pygame.draw.rect(gameWindow,
                             RED,
                             [food_x, food_y, snake_size, snake_size])
            pygame.draw.line(gameWindow,
                             RED,
                             (0, 40),
                             (SCREEN_WIDTH, 40),
                             5)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list) > snake_size:
                del snk_list[0]

            if snake_x < 0 or snake_x > SCREEN_WIDTH or snake_y < 50 or snake_y > SCREEN_HEIGHT:
                print("Game Over 2")

            plot_snake(gameWindow, BLACK, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    sys.exit()


game_loop()
