sx = 0 
sy = 0 
WIDTH = 918
HEIGHT = 203
offsetwidth = 17
offsetheight = 17
tilecount = 0

print("Start")
while sy < HEIGHT:
    while sx < WIDTH:
        print(f"(x:{sx}, y:{sy})")
        sx += offsetwidth
        tilecount += 1
    sy += offsetheight
    sx = 0
print(f"Total tiles: {tilecount}")
print("Done")