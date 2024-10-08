'''Test updown_tri.py'''
import unittest
from updown_tri import *  # pylint: disable=wildcard-import,unused-wildcard-import


class TestUpDownTri(unittest.TestCase):
    ''' Tests for updown_tri.py '''
    def atest_line_intersect(self):
        '''Test tri_line_intersect'''
        x1, y1 = tri_center(0, 1, 0)
        x2, y2 = tri_center(1, 1, 0)
        self.assertListEqual(list(tri_line_intersect(x1, y1, x2, y2)), [
            (0, 1, 0),
            (1, 1, 0),
        ])

        x1, y1 = tri_center(0, 1, 0)
        x2, y2 = tri_center(2, -1, 1)
        self.assertListEqual(list(tri_line_intersect(x1, y1, x2, y2)), [
            (0, 1, 0),
            (1, 1, 0),
            (1, 0, 0),
            (1, 0, 1),
            (1, -1, 1),
            (2, -1, 1),
        ])

        x1, y1 = tri_center(0, 1, 0)
        x2, y2 = tri_center(2, 0, -1)
        self.assertListEqual(list(tri_line_intersect(x1, y1, x2, y2)), [
            (0, 1, 0),
            (1, 1, 0),
            (1, 1, -1),
            (2, 1, -1),
            (2, 0, -1)
        ])

    def test_line(self):
        ''' Test tri_line'''
        self.assertListEqual(list(tri_line(1, 0, 1, 2, 0, 0)), [
            (1, 0, 1),
            (1, 0, 0),
            (2, 0, 0),
        ])

    def test_rect_intersect(self):
        ''' Test tri_rect_intersect'''
        x1, y1 = tri_center(0, 1, 0)
        self.assertListEqual(list(tri_rect_intersect(x1, y1, 0, 0)), [
            (0, 1, 0)
        ])
        self.assertListEqual(list(tri_rect_intersect(x1, y1, 0, 0.3)), [
            (0, 1, 0),
            (0, 2, 0),
        ])
        self.assertListEqual(list(tri_rect_intersect(x1, y1, 0.6, 0.3)), [
            (0, 1, 0),
            (1, 1, 0),
            (1, 1, -1),
            (0, 2, 0),
            (0, 2, -1),
            (1, 2, -1),
        ])

    def test_reflect(self):
        '''Test tri_reflect_x, tri_reflect_y, tri_reflect_by'''
        self.assertEqual(tri_reflect_x(1, 1, 0), (0, 1, 1))
        self.assertEqual(tri_reflect_y(1, 1, 0), (1, 0, 0))
        self.assertEqual(tri_reflect_by(1, 1, 0, 1), (1, 1, 0))
        self.assertEqual(tri_reflect_by(1, 1, 0, -1), (1, 0, 1))


if __name__ == '__main__':
    unittest.main()
