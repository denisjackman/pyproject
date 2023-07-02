'''
    bejewel game
'''

import random
import sys
import pygame
from pygame.locals import (KEYUP,
                           K_LEFT,
                           DOUBLEBUF,
                           K_RIGHT,
                           K_DOWN,
                           K_UP,
                           QUIT,
                           K_SPACE)

pygame.init()

NUM_SHAPES = 7         #7
PUZZLE_COLUMNS = 6     #6
PUZZLE_ROWS = 12       #12
SHAPE_WIDTH = 50       #50
SHAPE_HEIGHT = 50      #50

FPS = 15
WINDOW_WIDTH = PUZZLE_COLUMNS * SHAPE_WIDTH
WINDOW_HEIGHT = PUZZLE_ROWS * SHAPE_HEIGHT + 75

BACKGROUND = pygame.image.load("images/bg.png")

CIRCLE = pygame.image.load("images/circle.png")
DIAMOND = pygame.image.load("images/diamond.png")
HEXAGON = pygame.image.load("images/hexagon.png")
SQUARE = pygame.image.load("images/square.png")
STAR = pygame.image.load("images/star.png")
STAR2 = pygame.image.load("images/star2.png")
TRIANGLE = pygame.image.load("images/triangle.png")
SHAPES_LIST = [CIRCLE, DIAMOND, HEXAGON, SQUARE, STAR, STAR2, TRIANGLE]

for x in range(len(SHAPES_LIST) - NUM_SHAPES):
    del SHAPES_LIST[0]

EXPLOSION_1 = pygame.image.load("images/explosion1.png")
EXPLOSION_2 = pygame.image.load("images/explosion2.png")
EXPLOSION_3 = pygame.image.load("images/explosion3.png")
EXPLOSION_4 = pygame.image.load("images/explosion4.png")
EXPLOSION_5 = pygame.image.load("images/explosion5.png")
EXPLOSION_6 = pygame.image.load("images/explosion6.png")
EXPLOSION_LIST = [EXPLOSION_1, EXPLOSION_2, EXPLOSION_3, EXPLOSION_4,
                  EXPLOSION_5, EXPLOSION_6]

BLANK = pygame.image.load("images/blank.png")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FONT_SIZE = 36
TEXT_OFFSET = 5

MINIMUM_MATCH = 3
SINGLE_POINTS = .9
DOUBLE_POINTS = 3
TRIPLE_POINTS = 9
EXTRA_LENGTH_POINTS = .1
RANDOM_POINTS = .3
DELAY_PENALTY_SECONDS = 10
DELAY_PENALTY_POINTS = .5

FPS_CLOCK = pygame.time.Clock()
DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF)
pygame.display.set_caption("Bilging Puzzle")
SCORE = 0.0
SELECTOR = (0, 0)

def main():
    '''
        main routine
    '''
    global SCORE  # pylint: disable=W0603
    global SELECTOR  # pylint: disable=W0603
    bilgeBoard = generate_random_board()
    SELECTOR = (0, 0)
    SCORE = 0.0
    lastMoveTime = pygame.time.get_ticks()

    blit_board(bilgeBoard)
    draw_SELECTOR(SELECTOR)
    remove_matches(bilgeBoard, SELECTOR)

    blit_board(bilgeBoard)
    blit_score(SCORE)
    blit_time(0)
    draw_SELECTOR(SELECTOR)
    moveDelay = 0
    while True:
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_RIGHT and SELECTOR[0] < (PUZZLE_COLUMNS - 2):
                    SELECTOR = (SELECTOR[0] + 1, SELECTOR[1])
                if event.key == K_LEFT and SELECTOR [0] > 0:
                    SELECTOR = (SELECTOR[0] - 1, SELECTOR[1])
                if event.key == K_DOWN and SELECTOR[1] < (PUZZLE_ROWS - 1):
                    SELECTOR = (SELECTOR[0], SELECTOR[1] + 1)
                if event.key == K_UP and SELECTOR[1] > 0:
                    SELECTOR = (SELECTOR[0], SELECTOR[1] - 1)
                if event.key == K_SPACE:
                    lastMoveTime = pygame.time.get_ticks()

                    SCORE -= 1
                    swap_pieces(SELECTOR, bilgeBoard)
                    remove_matches(bilgeBoard, SELECTOR)

                    if moveDelay / (DELAY_PENALTY_SECONDS * 1000) >= 1:
                        score -= DELAY_PENALTY_POINTS * (moveDelay / (DELAY_PENALTY_SECONDS * 1000))

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        moveDelay = pygame.time.get_ticks() - lastMoveTime

        blit_board(bilgeBoard)
        blit_score(SCORE)
        blit_time(moveDelay / 1000)
        draw_SELECTOR(SELECTOR)

        pygame.display.update()
        FPS_CLOCK.tick(FPS)

def generate_random_board():
    '''
        generate random board
    '''
    return[ [SHAPES_LIST[random.randrange(0, len(SHAPES_LIST))] for i in range(PUZZLE_COLUMNS)] for x in range(PUZZLE_ROWS) ]

def blit_time(time):
    '''
        blit time
        Time in seconds since last move
    '''
    font = pygame.font.Font(None, FONT_SIZE)
    text = font.render("Move Timer: " + str(time / 60) + ":" + str(time % 60).zfill(2), True, BLACK)
    textPosition = text.get_rect()
    DISPLAY_SURFACE.blit(text, (TEXT_OFFSET, WINDOW_HEIGHT - (FONT_SIZE * 2)))

def blit_score(display_score):
    '''
        blit score
    '''
    font = pygame.font.Font(None, FONT_SIZE)
    text = font.render("Score: " + str(display_score), True, BLACK)
    textPosition = text.get_rect()
    DISPLAY_SURFACE.blit(text, (TEXT_OFFSET, WINDOW_HEIGHT - FONT_SIZE))

def blit_board(board):
    '''
        blit board
    '''
    DISPLAY_SURFACE.blit(BACKGROUND, (0, 0))
    rowNum = 0
    for row in board:
        columnNum = 0
        for shape in row:
            DISPLAY_SURFACE.blit(shape, (SHAPE_WIDTH * columnNum, SHAPE_HEIGHT * rowNum))
            columnNum += 1
        rowNum += 1

def draw_SELECTOR(position):
    '''
        Accepts a tuple indicating the position of the left shape in the
        SELECTOR relative to the board (as an array) (row, column)
    '''
    topLeft = (position[0] * SHAPE_WIDTH, position[1] * SHAPE_HEIGHT)
    topRight = (topLeft[0] + SHAPE_WIDTH * 2, topLeft[1])
    bottomLeft = (topLeft[0], topLeft[1] + SHAPE_HEIGHT)
    bottomRight = (topRight[0], topRight[1] + SHAPE_HEIGHT)
    pygame.draw.lines(DISPLAY_SURFACE, WHITE, True, [topLeft, topRight, bottomRight, bottomLeft], 3)

def swap_pieces(position, board):
    '''
        Accepts a tuple indicating the position of the SELECTOR
    '''
    pos_x, pos_y = position
    board[pos_y][pos_x + 1], board[pos_y][pos_x] = board[pos_y][pos_x], board[pos_y][pos_x + 1]

def remove_matches(board, match_SELECTOR):
    '''
        match removal
    '''
    matches = find_matches(board)

    while matches:
        explosion_animation(board, matches)
        score_matches(match_SELECTOR, matches)
        clear_matches(board, matches)
        refill_columns(board)
        matches = find_matches(board)
        match_SELECTOR = (0, 0)
        #So subsequent matches won't be counted as player matches

def score_matches(score_selector, matches):
    '''
        score
    '''
    global SCORE  # pylint: disable=W0603
    playerMatches = []

    score_selector = (score_selector[1], score_selector[0])

    for match in matches:
        for position in match:
            # if (position == score_selector or position == (score_selector[0], score_selector[1] + 1)) and (not match in playerMatches):
            #    playerMatches.append(match)
            if position in (score_selector, score_selector[0], score_selector[1] + 1) and (not match in playerMatches):
                playerMatches.append(match)

    if len(playerMatches) == 1:
        SCORE += SINGLE_POINTS
    elif len(playerMatches) == 2:
        SCORE += DOUBLE_POINTS
    elif len(playerMatches) == 3:
        SCORE += TRIPLE_POINTS

    for match in playerMatches:
        SCORE += (len(match) - MINIMUM_MATCH) * EXTRA_LENGTH_POINTS

    for match in matches:
        if not match in playerMatches:
            SCORE += RANDOM_POINTS

def find_matches(board):
    '''
        find matches
    '''
    clearList = []

    #First scan the columns for matches
    for column in range(PUZZLE_COLUMNS):
        length = 1
        for row in range(1, PUZZLE_ROWS):
            if board[row][column] == board[row - 1][column]:
                length += 1

            if not board[row][column] == board[row - 1][column]:
                if length >= MINIMUM_MATCH:
                    match = []
                    for clearRow in range(row - length, row):
                        match.append((clearRow, column))
                    clearList.append(match)
                length = 1

            if row == PUZZLE_ROWS - 1:
                if length >= MINIMUM_MATCH:
                    match = []
                    for clearRow in range(row - (length - 1), row + 1):
                        match.append((clearRow, column))
                    clearList.append(match)

    #Next scan the rows for matches
    for row in range(PUZZLE_ROWS):
        length = 1
        for column in range(1, PUZZLE_COLUMNS):
            if board[row][column] == board[row][column - 1]:
                length += 1

            if not board[row][column] == board[row][column - 1]:
                if length >= MINIMUM_MATCH:
                    match = []
                    for clearColumn in range(column - length, column):
                        match.append((row, clearColumn))
                    clearList.append(match)
                length = 1

            if column == PUZZLE_COLUMNS - 1:
                if length >= MINIMUM_MATCH:
                    match = []
                    for clearColumn in range(column - (length - 1), column + 1):
                        match.append((row, clearColumn))
                    clearList.append(match)

    return clearList

def clear_matches(board, matches):
    '''
        Accepts list of positions to clear
    '''
    for match in matches:
        for position in match:
            row, column = position
            board[row][column] = BLANK

def refill_columns(board):
    '''
        refill columns
    '''
    for column in range(PUZZLE_COLUMNS):
        for row in range(PUZZLE_ROWS):
            if board[row][column] == BLANK:
                test = 0
                length = 0

                #Determine how long the clear is
                while row + test < PUZZLE_ROWS and board[row + test][column] == BLANK:
                    length += 1
                    test += 1

                for blankRow in range(row, PUZZLE_ROWS):
                    try:
                        board[blankRow][column] = board[blankRow + length][column]
                    except Exception as err:
                        board[blankRow][column] = SHAPES_LIST[random.randrange(0, len(SHAPES_LIST))]
                        print(f' error {err}')


def explosion_animation(board, matches):
    '''
        animation
    '''
    for frame in EXPLOSION_LIST:
        for match in matches:
            for position in match:
                row, column = position
                board[row][column] = frame
        blit_board(board)
        pygame.display.update()
        FPS_CLOCK.tick(FPS)
