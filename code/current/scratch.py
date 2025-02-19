'''
    this is a scratch pad program to test out some code
'''
SX = 0
SY = 0
WIDTH = 918
HEIGHT = 203
OFFSETWIDTH = 17
OFFSETHEIGHT = 17
TILECOUNT = 0

print("Start")
while SY < HEIGHT:
    while SX < WIDTH:
        print(f"(x:{SX}, y:{SY})")
        SX += OFFSETWIDTH
        TILECOUNT += 1
    SY += OFFSETHEIGHT
    SX = 0
print(f"Total tiles: {TILECOUNT}")
print("Done")
