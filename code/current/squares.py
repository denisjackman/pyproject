''' squares.py'''
import simpleguitk as simplegui

CLICK = False
CX = 0
CY = 0


def new_game():
    ''' helper function to initialize globals'''
    # helper function to initialize globals
    return


def mouseclick(pos):
    '''' event handler for mouse CLICKs'''
    # define event handlers
    # pylint: disable=W0603
    global CX, CY, CLICK
    # add game state logic here
    CX = (pos[0] - (pos[0] % 50))/50
    CY = (pos[1] - (pos[1] % 50))/50
    CLICK = True


def draw(canvas):
    ''' draw handler'''
    x = 0
    y = 0
    for px in range(50):
        for py in range(20):
            canvas.draw_polygon([(x, y),
                                 (x+50, y),
                                 (x+50, y+50),
                                 (x, y+50)],
                                2,
                                "Red")
            y += 50
        x += 50
        y = 0
    if CLICK:
        vx = CX*50
        vy = CY*50
        canvas.draw_polygon([(vx, vy),
                             (vx+50, vy),
                             (vx+50, vy+50),
                             (vx, vy+50)],
                            2,
                            "Red",
                            "Green")


def main():
    ''' main function'''
    frame = simplegui.create_frame("Example", 1000, 750)
    frame.set_mouseclick_handler(mouseclick)
    frame.set_draw_handler(draw)

    new_game()
    frame.start()


if __name__ == '__main__':
    main()
