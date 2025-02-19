'''Test the square grid.'''''
import unittest
from flat_topped_hex import *  # pylint: disable=wildcard-import,unused-wildcard-import
from square import square_line


class TestSquare(unittest.TestCase):
    '''Tests for square.py'''
    def test_line(self):
        '''Test square_line'''
        self.assertListEqual(list(square_line(0, 0, 0, 5)), [
            (0, 0),
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (0, 5),
        ])


if __name__ == '__main__':
    unittest.main()
