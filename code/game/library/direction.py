"""
direction.py

This function provides all direction checking for any item as needed.

"""

__author__ = "Denis Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2015/12/02 16:00:00 $"
__copyright__ = "Copyright (c) 2015 jackmaninamtion"
__license__ = "Python"


def direction(position, direction_travel, wrap=True):
    """
    This function takes the current X,Y and direction of travel
    and returns a new X,Y based on these.
    :param position : This is a tuple which contains the
    X,Y position of an object
                        X = This is a positive number between zero (0)
                            and the width limit of the screen or board.
                        Y = This is a positive number between zero (0)
                            and the height limit of the screen or board.
    :param direction_travel: This is the direction of travel expressed
                             as a key work "UP", "DOWN", "LEFT", "RIGHT" etc.
    :param wrap: a boolean set to True if the width or height can wrap around
                 to the other side (default is True)
    :return:    new_x the new x co-ordinate
                new_y the new y co-ordinate
    """
    new_x = 0
    new_y = 0

    direction_x = position[0]
    direction_y = position[1]

    direction_travel = direction_travel.upper()
    if direction_travel not in ("UP",
                                'U',
                                'N',
                                'NORTH',
                                'DOWN',
                                'D',
                                'S',
                                'SOUTH',
                                'LEFT',
                                'L',
                                'W',
                                'WEST',
                                'RIGHT',
                                'R',
                                'E',
                                'EAST'):
        print(f'Wrong Way {direction_travel}')
        return direction_x, direction_y

    if direction_travel in ('UP', 'U', 'N', 'NORTH'):
        # This should be heading towards the 0 y axis
        new_x = direction_x
        new_y = direction_y - 1

    if direction_travel in ('DOWN', 'D', 'S', 'SOUTH'):
        # This should be heading towards the height limit y axis
        new_x = direction_x
        new_y = direction_y + 1

    if direction_travel in ('LEFT', 'L', 'W', 'WEST'):
        # This should be heading towards the 0 x axis
        new_x = direction_x - 1
        new_y = direction_y

    if direction_travel in ('RIGHT', 'R', 'E', 'EAST'):
        # This should be heading towards the width limit x axis

        new_x = direction_x + 1
        new_y = direction_y

    # TODO: Check for wrapping and act accordingly.
    if not wrap:
        print("not wrapping")

    return new_x, new_y


def main():
    ''' main function '''
    x = (1, 2)
    print(type(direction(x, 'Up')))
    x = direction(x, 'Up')
    print(direction(x, 'N'))
    x = direction(x, 'North')
    print(direction(x, 'down'))
    x = direction(x, 'S')
    print(direction(x, 'South'))
    x = direction(x, 'd')
    print(direction(x, 'W'))
    x = direction(x, 'West')
    print(direction(x, 'left'))
    x = direction(x, 'l')
    print(direction(x, 'right'))
    x = direction(x, 'r')
    print(direction(x, 'west'))
    x = direction(x, 'w')
    print(direction(x, 'wrong'))
    print(direction(x, 'wrong'))
    print(direction(x, 'wrong'))


if __name__ == '__main__':
    main()
