''' Test cases for hexutil.py'''
import unittest
import hexutil


class HexMap:
    ''' A map of hexagonal tiles.'''
    def __init__(self, hexstr):
        self.source = hexstr
        player = None
        target = None
        tiles = {}
        line_lengths = []
        lights = []
        for y, line in enumerate(hexstr.split("\n")):
            line_lengths.append(len(line))
            for x, ch in enumerate(line):
                if ch.isspace():
                    continue
                position = hexutil.Hex(x, y)
                if ch == '@':
                    player = position
                    ch = '.'
                elif ch == '%':
                    ch = '.'
                elif ch == 'T':
                    target = position
                elif ch == '*':
                    lights.append(position)
                tiles[position] = ch
        self.player = player
        self.target = target
        self.tiles = tiles
        self.line_lengths = line_lengths
        self.lights = lights

    def is_transparent(self, pos):
        ''' Is the tile at pos transparent?'''
        return self.tiles.get(pos, '#') != '#'

    def is_passable(self, pos):
        ''' Is the tile at pos passable?'''
        return self.tiles.get(pos, '#') not in "#~"

    def field_of_view(self, max_distance):
        ''' Return a dict of visible tiles.'''
        return self.player.field_of_view(transparent=self.is_transparent,
                                         max_distance=max_distance)

    def get_map(self, max_distance=None, path=frozenset()):
        ''' Return a string representation of the map.'''
        if max_distance is not None:
            fov = self.field_of_view(max_distance)
            if self.lights:
                light_fov = {}
                for light in self.lights:
                    light.field_of_view(transparent=self.is_transparent,
                                        max_distance=max_distance,
                                        visible=light_fov)
            else:
                light_fov = fov
        else:
            fov = light_fov = None
        lines = []
        for y, line_length in enumerate(self.line_lengths):
            line = []
            for x in range(line_length):
                if (x + y) % 2 != 0:
                    ch = ' '
                else:
                    pos = hexutil.Hex(x, y)
                    if pos == self.player:
                        ch = '@'
                    elif fov is None or (fov.get(pos, 0) & light_fov.get(pos, 0)):
                        if pos in path:
                            ch = '%'
                        else:
                            ch = self.tiles.get(pos, ' ')
                    else:
                        ch = ' '
                line.append(ch)
            lines.append("".join(line).rstrip())
        return "\n".join(lines)


testmap1 = HexMap("""
 # # # # # # # # #
# # # # # # # # # #
 # . # # # # # # #
# # . # # # # # # #
 # # # . . . . # #
# # # . @ # # . # #
 # # ~ % . # # . #
# # ~ # % # # # # #
 # # T % # # # # #
# # # # # # # # # #
""")

TESTMAP1_OUT = """



      # # # #
     # . . .
    # . @ #
   # ~ . . #
  # ~ # . #
   #   . #
      # #
"""

testmap2 = HexMap("""
 # # # # # # # # #
# # # # # # # # # #
 # . # # # * # # #
# # . # # . # # # #
 # # # . % % % # #
# # . . @ # # % # #
 # . # . # # # T #
# # # # . . # # # #
 # # . . . . # # #
# # # # # # # # # #
""")

TESTMAP2_OUT = """

          # #
           * #
          .
       . . .
      . @
     # . #
      # .


"""


class TestHex(unittest.TestCase):
    ''' Test cases for hexutil.Hex.'''

    def test_is_valid(self):
        ''' Test that hexutil.Hex raises an exception for invalid hexes.'''
        hexutil.Hex(-1, -3)
        self.assertRaises(hexutil.InvalidHex, hexutil.Hex, 2, -3)

    def test_rotations(self):
        ''' Test that hexutil.Hex.rotations returns the correct rotations.'''
        trhex = hexutil.Hex(2, 0)
        self.assertEqual([r(trhex) for r in hexutil.Hex.rotations], hexutil.origin.neighbours())

    def test_add(self):
        ''' Test that hexutil.Hex.__add__ and hexutil.Hex.__sub__ work.'''
        self.assertEqual(hexutil.Hex(2, 4) + hexutil.Hex(4, 6), hexutil.Hex(6, 10))

    def test_sub(self):
        ''' Test that hexutil.Hex.__add__ and hexutil.Hex.__sub__ work.'''
        self.assertEqual(hexutil.Hex(2, 4) - hexutil.Hex(3, 7), hexutil.Hex(-1, -3))

    def test_neg(self):
        ''' Test that hexutil.Hex.__neg__ works.'''
        self.assertEqual(-hexutil.Hex(2, 4), hexutil.Hex(-2, -4))
        self.assertEqual(-hexutil.origin, hexutil.origin)

    def test_neighbours(self):
        ''' Test that hexutil.Hex.neighbours returns the correct neighbours.'''
        origin = hexutil.origin
        nb = origin.neighbours()
        self.assertEqual(len(nb), 6)
        for h in nb:
            self.assertTrue((-h) in nb)
            self.assertTrue(origin in h.neighbours())

    def test_distance(self):
        ''' Test that hexutil.Hex.distance returns the correct distances.'''
        h = hexutil.Hex(-1, -3)
        for nb in h.neighbours():
            self.assertEqual(nb.distance(nb), 0)
            self.assertEqual(nb.distance(h), 1)
            self.assertEqual(max(nb2.distance(h) for nb2 in nb.neighbours()), 2)

    def test_rotate_left(self):
        '''
        Test that hexutil.Hex.rotate_left returns the correct neighbours.
        '''
        origin = hexutil.origin
        neighbours = origin.neighbours()
        nb = neighbours[0]
        neighbours2 = []
        for i in range(6):
            neighbours2.append(nb)
            nb = nb.rotate_left()
        self.assertEqual(neighbours, neighbours2)

    def test_rotate_right(self):
        '''
        Test that hexutil.Hex.rotate_right returns the correct neighbours.
        '''
        # origin = hexutil.origin
        for nb in hexutil.origin.neighbours():
            self.assertEqual(nb.rotate_left().rotate_right(), nb)


class TestHexGrid(unittest.TestCase):
    ''' Test cases for hexutil.HexGrid.'''
    def test_height(self):
        ''' Test that hexutil.HexGrid.height returns the correct height.'''
        self.assertEqual(hexutil.HexGrid(32).height, 18)

    def test_corners(self):
        ''' Test that hexutil.HexGrid.corners returns the correct corners.'''
        self.assertEqual(hexutil.HexGrid(32).corners(hexutil.Hex(1, 1)),
                         [(64, 72),
                          (32, 90),
                          (0, 72),
                          (0, 36),
                          (32, 18),
                          (64, 36)])

    def test_hex_at_coordinates(self):
        '''
        Test that hexutil.HexGrid.hex_at_coordinate returns the correct hexes.
        '''
        hg = hexutil.HexGrid(32)
        data = [
                ((0, 0), hexutil.Hex(0, 0)),
                ((33, 16), hexutil.Hex(2, 0)),
                ((30, 20), hexutil.Hex(1, 1))
                ]
        for fx in (-1, 1):
            for fy in (-1, 1):
                for pixel, pxhex in data:
                    x, y = pixel
                    pixel = (fx*x, fy*y)
                    x, y = pxhex
                    pxhex = hexutil.Hex(fx*x, fy*y)
                    self.assertEqual(hg.hex_at_coordinate(*pixel),
                                     pxhex,
                                     pixel)

    def test_center(self):
        ''' Test that hexutil.HexGrid.center returns the correct centers.'''
        hg = hexutil.HexGrid(32)
        self.assertEqual(hg.center(hexutil.Hex(1, 1)), (32, 54))

    def test_bounding_box(self):
        '''
        Test that hexutil.HexGrid.bounding_box returns the
        correct bounding boxes.
        '''
        hg = hexutil.HexGrid(32)
        self.assertEqual(hg.bounding_box(hexutil.Hex(0, 2)),
                         hexutil.Rectangle(-32, 72, 64, 72))

    def test_hexes_in_rectangle(self):
        '''
        Test that hexutil.HexGrid.hexes_in_rectangle returns
        the correct hexes.
        '''
        hg = hexutil.HexGrid(32)
        self.assertEqual(
                list(hg.hexes_in_rectangle(hg.bounding_box(hexutil.origin))),
                [hexutil.Hex(-1, -1), hexutil.Hex(1, -1),
                 hexutil.Hex(-2, 0), hexutil.Hex(0, 0),
                 hexutil.Hex(-1, 1), hexutil.Hex(1, 1)]
                )


class TestFov(unittest.TestCase):
    ''' Test cases for fov.Fov.'''
    def test_fov1(self):
        ''' Test that fov.Fov.get_map returns the correct map.'''
        self.assertEqual(testmap1.get_map(10), TESTMAP1_OUT)

    def test_fov2(self):
        ''' Test that fov.Fov.get_map returns the correct map.'''
        self.assertEqual(testmap2.get_map(10), TESTMAP2_OUT)


class TestPathFinding(unittest.TestCase):
    ''' Test cases for pathfinding.PathFinding.'''
    def test_path1(self):
        '''
        Test that pathfinding.PathFinding.find_path returns the correct path.
        '''
        path = frozenset(testmap1.player.find_path(testmap1.target,
                                                   testmap1.is_passable)[:-1])
        self.assertEqual(testmap1.get_map(path=path), testmap1.source)

    def test_path2(self):
        '''
        Test that pathfinding.PathFinding.find_path returns the correct path.
        '''
        path = frozenset(testmap2.player.find_path(testmap2.target,
                                                   testmap2.is_passable)[:-1])
        self.assertEqual(testmap2.get_map(path=path), testmap2.source)


if __name__ == '__main__':
    unittest.main()
