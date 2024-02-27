'''
    hex utilities
'''
HEIGHT = 100
WIDTH = 100
QUARTER = 4
HALF = 2


def get_co_ords(tile_type, pos):  # pylint: disable=R0914
    '''
        get the go ords
    '''
    x = pos[0]
    y = pos[1]
    if tile_type == "FLATHEX":
        # this generates the points for a flat top hex
        # the next hex starts at X = X+(WIDTH/4)*3 and Y = Y+HEIGHT/2
        x1 = x + (WIDTH / QUARTER)
        x2 = x + ((WIDTH / QUARTER) * 3)
        x3 = x + WIDTH
        x4 = x + ((WIDTH / QUARTER) * 3)
        x5 = x + (WIDTH / QUARTER)
        x6 = x

        y1 = y
        y2 = y
        y3 = y + (HEIGHT / HALF)
        y4 = y + HEIGHT
        y5 = y + HEIGHT
        y6 = y + (HEIGHT / HALF)
        result = [(x1, y1),
                  (x2, y2),
                  (x3, y3),
                  (x4, y5),
                  (x5, y5),
                  (x6, y6)]
    elif tile_type == "POINTHEX":
        # This generates a pointy top hex
        # the next row of hexs start at X = X+(WIDTH/2)  Y=Y+(HEIGHT/4)*3)
        x1 = x + (WIDTH / HALF)
        x2 = x + WIDTH
        x3 = x + WIDTH
        x4 = x + (WIDTH / HALF)
        x5 = x
        x6 = x
        y1 = y
        y2 = y + (HEIGHT / QUARTER)
        y3 = y + ((HEIGHT / QUARTER) * 3)
        y4 = y + HEIGHT
        y5 = y + ((HEIGHT / QUARTER) * 3)
        y6 = y + (HEIGHT / QUARTER)
        result = [(x1, y1),
                  (x2, y2),
                  (x3, y3),
                  (x4, y5),
                  (x5, y5),
                  (x6, y6)]
    else:
        # assume that we need a square
        x1 = x
        x2 = x + WIDTH
        x3 = x + WIDTH
        x4 = x
        y1 = y
        y2 = y
        y3 = y + HEIGHT
        y4 = y + HEIGHT
        result = [(x1, y1),
                  (x2, y2),
                  (x3, y3),
                  (x4, y4)]
    return result


def main():
    '''
        main function
    '''
    print(get_co_ords("POINTHEX", (0, 0)))
    print(get_co_ords("FLATHEX", (0, 0)))
    print(get_co_ords("NOHEX", (0, 0)))


if __name__ == '__main__':
    main()
