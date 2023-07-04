import simplegui
click = False


def new_game():
    # helper function to initialize globals
    return


def mouseclick(pos):
    # define event handlers
    global cx, cy, click
    # add game state logic here
    cx = (pos[0] - (pos[0] % 50))/50
    cy = (pos[1] - (pos[1] % 50))/50
    click = True
    return


def draw(canvas):
    global cx, cy, click
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
    if click:
        vx = cx*50
        vy = cy*50
        canvas.draw_polygon([(vx, vy),
                             (vx+50, vy),
                             (vx+50, vy+50),
                             (vx, vy+50)],
                            2,
                            "Red",
                            "Green")
    return


frame = simplegui.create_frame("Example", 1000, 750)
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()
