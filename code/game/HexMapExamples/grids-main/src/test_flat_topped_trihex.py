'''Test flat_topped_trihex.py'''
import unittest
from flat_topped_trihex import *  # pylint: disable=wildcard-import,unused-wildcard-import


class TestFlatToppedTriHex(unittest.TestCase):
    '''Tests for flat_topped_trihex.py'''
    def test_pick(self):
        '''Test pick_trihex'''
        for (a, b, c) in [(0, 0, 0),
                          (0, 1, 0),
                          (5, -2, -3),
                          (-3, 0, 2)]:
            self.assertEqual(pick_trihex(*trihex_center(a, b, c)),
                             (a, b, c))

    def test_tri_convert(self):
        '''Test trihex_to_tris and tri_to_trihex'''
        for (a, b, c) in [(0, 0, 0),
                          (0, 1, 0),
                          (5, -2, -3),
                          (-3, 0, 2)]:
            for tri in trihex_to_tris(a, b, c):
                self.assertEqual(tri_to_trihex(*tri), (a, b, c))


if __name__ == '__main__':
    unittest.main()
