''' Module: Hex_Math.py            2/16/2009
    Author: John Crawford

    Contains various hexagon manipulation code.
    I originally decided to base the computations on the width and height
    of a Hex, being mathematically correct:
    Height = Diameter * cos(30 degrees), = 0.866
    But numerous experiments convinced me that the visual effect is not as
    clear as a different ratio of height = diameter * 0.93, given that
    crt/lcd screen pixels are not perfect squares...
    There are six points defining the hex, top/middle/bottom - left/right:
    '''

import wx
ACROSS, DOWN = 0, 1

def ComputeHexPoints(d, h, dir, closed=False, setborder=False):
    ''' TODO: to allow for a thicker border line, the points have to form
        a smaller hex. '''
    if setborder:
        border = 3
    else:
        border = 0
    if dir == ACROSS:
        return _ComputeHexPointsAcross(d, h, closed, border)
    else:
        return _ComputeHexPointsDown(d, h, closed, border)

def _ComputeHexPointsDown(d, h, closed, border):
    ''' Computes hex points TopLeft, TopRight, MiddleLeft, MiddleRight,
        BottomLeft, BottomRight. 
        _____
       /     \
      /       \
      \       /
       \_____/
    '''
    diam = float(d)
    height = float(h)

    TL = (round(diam/4.0), 0 + border)
    TR = (round((diam * 3.0)/4.0) - 1, 0 + border)
    ML = (0 + border, round(height/2.0))
    MR = (diam - 1 - border, round(height/2.0) - 1)
    BL = (round(diam/4.0), height - 1 - border)
    BR = (round((diam * 3.0)/4.0) - 1, height - 1 - border)

    point_list = [TL, TR, MR, BR, BL, ML]
    if closed:
        point_list.append(TL)
    return point_list

def _ComputeHexPointsAcross(d, h, closed, border):
    ''' Computes hex points TopMiddle, RightTop, RightBottom,
        BottomMiddle, LeftBottom, LeftTop. 
        /\
       /  \
      /    \
     |      |
     |      |
     |      |
      \    /
       \  /
        \/
    '''
    diam = float(d)
    height = float(h)

    TM = (round(diam/2.0) - 1, 0 + border)
    RT = (diam - 1 - border, round(height/4.0))
    RB = (diam - 1 - border, round((height * 3.0)/4.0))
    BM = (round(diam/2.0), height - 1 - border)
    LB = (0 + border, round((height * 3.0)/4.0))
    LT = (0 + border, round(height/4.0))

    point_list = [TM, RT, RB, BM, LB, LT]
    if closed:
        point_list.append(TM)
    return point_list

def ShortestDist(rect, point):
    ''' Given a Rectangle and internal point, return distance from the
        point to the closest corner.'''

    def ComputeDist(p1, p2): # standard formula for distance between 2 points.
        from math import sqrt
        xdiff = float(p1[0]) - float(p2[0])
        ydiff = float(p1[1]) - float(p2[1])
        disc = sqrt(xdiff ** 2 + ydiff ** 2)
        return disc

    dist_list = []
    dist_list.append(ComputeDist(rect[0], point))
    dist_list.append(ComputeDist(rect[1], point))
    dist_list.append(ComputeDist(rect[2], point))
    dist_list.append(ComputeDist(rect[3], point))

    return min(dist_list)
