'''
    hex generation code from Amit Patel
'''
# Generated code --
# CC0 --
# No Rights Reserved --
# http://www.redblobgames.com/grids/hexagons/

from __future__ import division
from __future__ import print_function
import collections
import math

Point = collections.namedtuple("Point", ["x", "y"])
_Hex = collections.namedtuple("Hex", ["q", "r", "s"])


def Hex(q, r, s):
    ''' Hex(q, r, s) creates a new Hex object.'''
    assert not (round(q + r + s) != 0), "q + r + s must be 0"
    return _Hex(q, r, s)


def hex_add(a, b):
    '''
    hex_add(a, b) returns a new Hex object that is the
    sum of Hex objects a and b.
    '''
    return Hex(a.q + b.q, a.r + b.r, a.s + b.s)


def hex_subtract(a, b):
    '''
    hex_subtract(a, b) returns a new Hex object that
    is the difference of Hex objects a and b.
    '''
    return Hex(a.q - b.q, a.r - b.r, a.s - b.s)


def hex_scale(a, k):
    '''
    hex_scale(a, k) returns a new Hex object that is
    the product of Hex object a and scalar k.
    '''
    return Hex(a.q * k, a.r * k, a.s * k)


def hex_rotate_left(a):
    '''
    hex_rotate_left(a) returns a new Hex object that is
    the result of rotating Hex object a 60 degrees counter-clockwise.
    '''
    return Hex(-a.s, -a.q, -a.r)


def hex_rotate_right(a):
    '''
    hex_rotate_right(a) returns a new Hex object that is the
    result of rotating Hex object a 60 degrees clockwise.
    '''
    return Hex(-a.r, -a.s, -a.q)


hex_directions = [Hex(1, 0, -1),
                  Hex(1, -1, 0),
                  Hex(0, -1, 1),
                  Hex(-1, 0, 1),
                  Hex(-1, 1, 0),
                  Hex(0, 1, -1)]


def hex_direction(direction):
    '''
    hex_direction(direction) returns a new Hex object that is the
    direction of the given number.
    '''
    return hex_directions[direction]


def hex_neighbor(hnhex, direction):
    '''
    hex_neighbor(hex, direction) returns a new Hex object that is the
    neighbor of Hex object hex in the given direction.
    '''
    return hex_add(hnhex, hex_direction(direction))


hex_diagonals = [Hex(2, -1, -1),
                 Hex(1, -2, 1),
                 Hex(-1, -1, 2),
                 Hex(-2, 1, 1),
                 Hex(-1, 2, -1),
                 Hex(1, 1, -2)]


def hex_diagonal_neighbor(hdnhex, direction):
    '''
    hex_diagonal_neighbor(hex, direction) returns a new Hex object
    that is the neighbor of Hex object hex in the given diagonal direction.
    '''
    return hex_add(hdnhex, hex_diagonals[direction])


def hex_length(hlhex):
    ''' hex_length(hex) returns the length of the given Hex object.'''
    return (abs(hlhex.q) + abs(hlhex.r) + abs(hlhex.s)) // 2


def hex_distance(a, b):
    ''' hex_distance(a, b) returns the distance between Hex objects a and b.'''
    return hex_length(hex_subtract(a, b))


def hex_round(h):
    '''
    hex_round(h) returns a new Hex object that is the rounded version of
    Hex object h.
    '''
    qi = int(round(h.q))
    ri = int(round(h.r))
    si = int(round(h.s))
    q_diff = abs(qi - h.q)
    r_diff = abs(ri - h.r)
    s_diff = abs(si - h.s)
    if q_diff > r_diff and q_diff > s_diff:
        qi = -ri - si
    else:
        if r_diff > s_diff:
            ri = -qi - si
        else:
            si = -qi - ri
    return Hex(qi, ri, si)


def hex_lerp(a, b, t):
    '''
    hex_lerp(a, b, t) returns a new Hex object that is the linear
    interpolation between Hex objects a and b at time t.
    '''
    return Hex(a.q * (1.0 - t) + b.q * t,
               a.r * (1.0 - t) + b.r * t,
               a.s * (1.0 - t) + b.s * t)


def hex_linedraw(a, b):
    '''
    Hex_linedraw(a, b) returns a list of Hex objects that are on the
    line between Hex objects a and b.
    '''
    N = hex_distance(a, b)
    a_nudge = Hex(a.q + 1e-06, a.r + 1e-06, a.s - 2e-06)
    b_nudge = Hex(b.q + 1e-06, b.r + 1e-06, b.s - 2e-06)
    results = []
    step = 1.0 / max(N, 1)
    for i in range(0, N + 1):
        results.append(hex_round(hex_lerp(a_nudge,
                                          b_nudge,
                                          step * i)))
    return results


OffsetCoord = collections.namedtuple("OffsetCoord", ["col", "row"])

EVEN = 1
ODD = -1


def qoffset_from_cube(offset, h):
    '''
    qoffset_from_cube(offset, h) returns an OffsetCoord object that is
    the conversion of Hex object h to an offset coordinate.
    '''
    col = h.q
    row = h.r + (h.q + offset * (h.q & 1)) // 2
    if offset not in (EVEN, ODD):
        raise ValueError("offset must be EVEN (+1) or ODD (-1)")
    return OffsetCoord(col, row)


def qoffset_to_cube(offset, h):
    '''
    qoffset_to_cube(offset, h) returns a new Hex object that is the
    conversion of OffsetCoord object h to a cube coordinate.
    '''
    q = h.col
    r = h.row - (h.col + offset * (h.col & 1)) // 2
    s = -q - r
    if offset not in (EVEN, ODD):
        raise ValueError("offset must be EVEN (+1) or ODD (-1)")
    return Hex(q, r, s)


def roffset_from_cube(offset, h):
    '''
    roffset_from_cube(offset, h) returns an OffsetCoord object that is
    the conversion of Hex object h to an offset coordinate.
    '''
    col = h.q + (h.r + offset * (h.r & 1)) // 2
    row = h.r
    if offset not in (EVEN, ODD):
        raise ValueError("offset must be EVEN (+1) or ODD (-1)")
    return OffsetCoord(col, row)


def roffset_to_cube(offset, h):
    '''
    roffset_to_cube(offset, h) returns a new Hex object that is the
    conversion of OffsetCoord object h to a cube coordinate.
    '''
    q = h.col - (h.row + offset * (h.row & 1)) // 2
    r = h.row
    s = -q - r
    if offset not in (EVEN, ODD):
        raise ValueError("offset must be EVEN (+1) or ODD (-1)")
    return Hex(q, r, s)


DoubledCoord = collections.namedtuple("DoubledCoord", ["col", "row"])


def qdoubled_from_cube(h):
    '''
    qdoubled_from_cube(h) returns a DoubledCoord object that is the conversion
    of Hex object h to a doubled coordinate.
    '''
    col = h.q
    row = 2 * h.r + h.q
    return DoubledCoord(col, row)


def qdoubled_to_cube(h):
    '''
    qdoubled_to_cube(h) returns a new Hex object that is the conversion of
    DoubledCoord object h to a cube coordinate.
    '''
    q = h.col
    r = (h.row - h.col) // 2
    s = -q - r
    return Hex(q, r, s)


def rdoubled_from_cube(h):
    '''
    rdoubled_from_cube(h) returns a DoubledCoord object that is the conversion
    of Hex object h to a doubled coordinate.
    '''
    col = 2 * h.q + h.r
    row = h.r
    return DoubledCoord(col, row)


def rdoubled_to_cube(h):
    '''
    rdoubled_to_cube(h) returns a new Hex object that is the conversion of
    DoubledCoord object h to a cube coordinate.
    '''
    q = (h.col - h.row) // 2
    r = h.row
    s = -q - r
    return Hex(q, r, s)


Orientation = collections.namedtuple("Orientation",
                                     ["f0",
                                      "f1",
                                      "f2",
                                      "f3",
                                      "b0",
                                      "b1",
                                      "b2",
                                      "b3",
                                      "start_angle"])
Layout = collections.namedtuple("Layout",
                                ["orientation",
                                 "size",
                                 "origin"])
layout_pointy = Orientation(math.sqrt(3.0),
                            math.sqrt(3.0) / 2.0, 0.0,
                            3.0 / 2.0,
                            math.sqrt(3.0) / 3.0,
                            -1.0 / 3.0,
                            0.0,
                            2.0 / 3.0,
                            0.5)
layout_flat = Orientation(3.0 / 2.0,
                          0.0,
                          math.sqrt(3.0) / 2.0,
                          math.sqrt(3.0),
                          2.0 / 3.0,
                          0.0,
                          -1.0 / 3.0,
                          math.sqrt(3.0) / 3.0,
                          0.0)


def hex_to_pixel(layout, h):
    '''
    hex_to_pixel(layout, h) returns a Point object that is the conversion of
    Hex object h to a pixel coordinate.
    '''
    M = layout.orientation
    size = layout.size
    origin = layout.origin
    x = (M.f0 * h.q + M.f1 * h.r) * size.x
    y = (M.f2 * h.q + M.f3 * h.r) * size.y
    return Point(x + origin.x, y + origin.y)


def pixel_to_hex(layout, p):
    '''
    pixel_to_hex(layout, p) returns a new Hex object that is the conversion of
    Point object p to a hex coordinate.
    '''
    M = layout.orientation
    size = layout.size
    origin = layout.origin
    pt = Point((p.x - origin.x) / size.x, (p.y - origin.y) / size.y)
    q = M.b0 * pt.x + M.b1 * pt.y
    r = M.b2 * pt.x + M.b3 * pt.y
    return Hex(q, r, -q - r)


def hex_corner_offset(layout, corner):
    '''
    hex_corner_offset(layout, corner) returns a Point object that is the
    conversion of a corner number to a pixel offset.
    '''
    M = layout.orientation
    size = layout.size
    angle = 2.0 * math.pi * (M.start_angle - corner) / 6.0
    return Point(size.x * math.cos(angle), size.y * math.sin(angle))


def polygon_corners(layout, h):
    '''
    polygon_corners(layout, h) returns a list of Point objects that are
    the corners of the hexagon h.
    '''
    corners = []
    center = hex_to_pixel(layout, h)
    for i in range(0, 6):
        offset = hex_corner_offset(layout, i)
        corners.append(Point(center.x + offset.x, center.y + offset.y))
    return corners


def complain(name):
    '''
    complain(name) prints a failure message for the test named name.
    '''
    print(f"FAIL {name}")


def equal_hex(name, a, b):
    '''
    equal_hex(name, a, b) checks that a and b are equal Hex objects.
    '''
    if not (a.q == b.q and a.s == b.s and a.r == b.r):
        complain(name)


def equal_offsetcoord(name, a, b):
    '''
    equal_offsetcoord(name, a, b) checks that a and b are equal
    OffsetCoord objects.
    '''
    if not (a.col == b.col and a.row == b.row):
        complain(name)


def equal_doubledcoord(name, a, b):
    '''
    equal_doubledcoord(name, a, b) checks that a and b are equal
    DoubledCoord objects.
    '''
    if not (a.col == b.col and a.row == b.row):
        complain(name)


def equal_int(name, a, b):
    ''' equal_int(name, a, b) checks that a and b are equal integers.'''
    if not a == b:
        complain(name)


def equal_hex_array(name, a, b):
    '''
    equal_hex_array(name, a, b) checks that a and b are equal
    lists of Hex objects.
    '''
    equal_int(name, len(a), len(b))
    for i in range(0, len(a)):
        equal_hex(name, a[i], b[i])


def test_hex_arithmetic():
    ''' hex_add(a, b) returns the hex that is the sum of hexes a and b'''
    equal_hex("hex_add",
              Hex(4, -10, 6),
              hex_add(Hex(1, -3, 2),
                      Hex(3, -7, 4)))
    equal_hex("hex_subtract",
              Hex(-2, 4, -2),
              hex_subtract(Hex(1, -3, 2),
                           Hex(3, -7, 4)))


def test_hex_direction():
    ''' hex_direction(direction) returns the hex in the given direction'''
    equal_hex("hex_direction", Hex(0, -1, 1), hex_direction(2))


def test_hex_neighbor():
    '''
    hex_neighbor(a, direction) returns the hex that is adjacent to hex a
    in the given direction
    '''
    equal_hex("hex_neighbor", Hex(1, -3, 2), hex_neighbor(Hex(1, -2, 1), 2))


def test_hex_diagonal():
    '''
    hex_diagonal_neighbor(a, direction) returns the hex that is diagonally
    across from hex a in the given direction
    '''
    equal_hex("hex_diagonal",
              Hex(-1, -1, 2),
              hex_diagonal_neighbor(Hex(1, -2, 1), 3))


def test_hex_distance():
    ''' hex_distance(a, b) returns the number of hexes between hexes a and b'''
    equal_int("hex_distance", 7, hex_distance(Hex(3, -7, 4), Hex(0, 0, 0)))


def test_hex_rotate_right():
    '''
    hex_rotate_right(a) returns the hex that is a rotated right around the
    origin hex
    '''
    equal_hex("hex_rotate_right",
              hex_rotate_right(Hex(1, -3, 2)),
              Hex(3, -2, -1))


def test_hex_rotate_left():
    '''
    hex_rotate_left(a) returns the hex that is a rotated left around
    the origin hex
    '''
    equal_hex("hex_rotate_left",
              hex_rotate_left(Hex(1, -3, 2)),
              Hex(-2, -1, 3))


def test_hex_round():
    ''' hex_round(a) returns the nearest hex to a given hex coordinate'''
    a = Hex(0.0, 0.0, 0.0)
    b = Hex(1.0, -1.0, 0.0)
    c = Hex(0.0, -1.0, 1.0)
    equal_hex("hex_round 1",
              Hex(5, -10, 5),
              hex_round(hex_lerp(Hex(0.0, 0.0, 0.0),
                                 Hex(10.0, -20.0, 10.0), 0.5)))
    equal_hex("hex_round 2",
              hex_round(a),
              hex_round(hex_lerp(a, b, 0.499)))
    equal_hex("hex_round 3",
              hex_round(b),
              hex_round(hex_lerp(a, b, 0.501)))
    equal_hex("hex_round 4",
              hex_round(a),
              hex_round(Hex(a.q * 0.4 + b.q * 0.3 + c.q * 0.3,
                            a.r * 0.4 + b.r * 0.3 + c.r * 0.3,
                            a.s * 0.4 + b.s * 0.3 + c.s * 0.3)))
    equal_hex("hex_round 5",
              hex_round(c),
              hex_round(Hex(a.q * 0.3 + b.q * 0.3 + c.q * 0.4,
                            a.r * 0.3 + b.r * 0.3 + c.r * 0.4,
                            a.s * 0.3 + b.s * 0.3 + c.s * 0.4)))


def test_hex_linedraw():
    '''test_hex_linedraw'''
    equal_hex_array("hex_linedraw",
                    [Hex(0, 0, 0),
                     Hex(0, -1, 1),
                     Hex(0, -2, 2),
                     Hex(1, -3, 2),
                     Hex(1, -4, 3),
                     Hex(1, -5, 4)],
                    hex_linedraw(Hex(0, 0, 0),
                                 Hex(1, -5, 4)))


def test_layout():
    '''  test layout functions'''
    h = Hex(3, 4, -7)
    flat = Layout(layout_flat, Point(10.0, 15.0), Point(35.0, 71.0))
    equal_hex("layout",
              h,
              hex_round(pixel_to_hex(flat, hex_to_pixel(flat, h))))
    pointy = Layout(layout_pointy, Point(10.0, 15.0), Point(35.0, 71.0))
    equal_hex("layout", h, hex_round(pixel_to_hex(pointy,
                                                  hex_to_pixel(pointy, h))))


def test_offset_roundtrip():
    '''   h = Hex(3, 4, -7)'''
    a = Hex(3, 4, -7)
    b = OffsetCoord(1, -3)
    equal_hex("conversion_roundtrip even-q",
              a,
              qoffset_to_cube(EVEN, qoffset_from_cube(EVEN, a)))
    equal_offsetcoord("conversion_roundtrip even-q",
                      b,
                      qoffset_from_cube(EVEN,
                                        qoffset_to_cube(EVEN, b)))
    equal_hex("conversion_roundtrip odd-q",
              a,
              qoffset_to_cube(ODD, qoffset_from_cube(ODD, a)))
    equal_offsetcoord("conversion_roundtrip odd-q",
                      b,
                      qoffset_from_cube(ODD, qoffset_to_cube(ODD, b)))
    equal_hex("conversion_roundtrip even-r",
              a,
              roffset_to_cube(EVEN, roffset_from_cube(EVEN, a)))
    equal_offsetcoord("conversion_roundtrip even-r",
                      b,
                      roffset_from_cube(EVEN, roffset_to_cube(EVEN, b)))
    equal_hex("conversion_roundtrip odd-r",
              a,
              roffset_to_cube(ODD, roffset_from_cube(ODD, a)))
    equal_offsetcoord("conversion_roundtrip odd-r",
                      b,
                      roffset_from_cube(ODD, roffset_to_cube(ODD, b)))


def test_offset_from_cube():
    ''' Test offset_from_cube'''
    equal_offsetcoord("offset_from_cube even-q",
                      OffsetCoord(1, 3),
                      qoffset_from_cube(EVEN, Hex(1, 2, -3)))
    equal_offsetcoord("offset_from_cube odd-q",
                      OffsetCoord(1, 2),
                      qoffset_from_cube(ODD, Hex(1, 2, -3)))


def test_offset_to_cube():
    ''' Test offset_to_cube'''
    equal_hex("offset_to_cube even-",
              Hex(1, 2, -3),
              qoffset_to_cube(EVEN, OffsetCoord(1, 3)))
    equal_hex("offset_to_cube odd-q",
              Hex(1, 2, -3),
              qoffset_to_cube(ODD, OffsetCoord(1, 2)))


def test_doubled_roundtrip():
    '''Test doubled_roundtrip'''
    a = Hex(3, 4, -7)
    b = DoubledCoord(1, -3)
    equal_hex("conversion_roundtrip doubled-q",
              a,
              qdoubled_to_cube(qdoubled_from_cube(a)))
    equal_doubledcoord("conversion_roundtrip doubled-q",
                       b,
                       qdoubled_from_cube(qdoubled_to_cube(b)))
    equal_hex("conversion_roundtrip doubled-r",
              a,
              rdoubled_to_cube(rdoubled_from_cube(a)))
    equal_doubledcoord("conversion_roundtrip doubled-r",
                       b,
                       rdoubled_from_cube(rdoubled_to_cube(b)))


def test_doubled_from_cube():
    '''Test doubled_from_cube'''
    equal_doubledcoord("doubled_from_cube doubled-q",
                       DoubledCoord(1, 5),
                       qdoubled_from_cube(Hex(1, 2, -3)))
    equal_doubledcoord("doubled_from_cube doubled-r",
                       DoubledCoord(4, 2),
                       rdoubled_from_cube(Hex(1, 2, -3)))


def test_doubled_to_cube():
    '''Test doubled_to_cube'''
    equal_hex("doubled_to_cube doubled-q",
              Hex(1, 2, -3),
              qdoubled_to_cube(DoubledCoord(1, 5)))
    equal_hex("doubled_to_cube doubled-r",
              Hex(1, 2, -3),
              rdoubled_to_cube(DoubledCoord(4, 2)))


def test_all():
    '''Run all tests'''
    print("Testing hexagon functions")
    test_hex_arithmetic()
    test_hex_direction()
    test_hex_neighbor()
    test_hex_diagonal()
    test_hex_distance()
    test_hex_rotate_right()
    test_hex_rotate_left()
    test_hex_round()
    test_hex_linedraw()
    test_layout()
    test_offset_roundtrip()
    test_offset_from_cube()
    test_offset_to_cube()
    test_doubled_roundtrip()
    test_doubled_from_cube()
    test_doubled_to_cube()
    print("All tests passed")


if __name__ == '__main__':
    test_all()
