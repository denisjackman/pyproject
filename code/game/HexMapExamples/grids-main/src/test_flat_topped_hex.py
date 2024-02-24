'''Tests for flat_topped_hex.py'''
import unittest
from flat_topped_hex import *  # pylint: disable=wildcard-import,unused-wildcard-import  # noqa: F403, E501
from updown_tri import tri_center


class TestFlatToppedHex(unittest.TestCase):
    '''Tests for flat_topped_hex.py'''
    def test_rect1(self):
        '''Test hex_rect'''
        rect = (0, 0, 0, 3, 3, False, False)
        self.assertListEqual(list(hex_rect(*rect)), [  # noqa: F405
            (0, 0, 0),
            (0, 1, -1),
            (0, 2, -2),
            (1, 0, -1),
            (1, 1, -2),
            (2, -1, -1),
            (2, 0, -2),
            (2, 1, -3),
        ])

        i = 0
        for hrhex in hex_rect(*rect):  # noqa: F405
            self.assertEqual(hex_rect_index(*hrhex, *rect), i)  # noqa: F405
            self.assertEqual(hex_rect_deindex(i, *rect), hrhex)  # noqa: F405
            i += 1

        self.assertEqual(len(list(hex_rect(*rect))),  # noqa: F405
                         hex_rect_size(*rect))  # noqa: F405

    def test_rect2(self):
        '''Test hex_rect'''
        rect = (0, 0, 0, 3, 3, True, True)
        self.assertListEqual(list(hex_rect(*rect)), [  # noqa: F405
            (0, 0, 0),
            (0, 1, -1),
            (0, 2, -2),
            (1, -1, 0),
            (1, 0, -1),
            (1, 1, -2),
            (1, 2, -3),
            (2, -1, -1),
            (2, 0, -2),
            (2, 1, -3),
        ])

        i = 0
        for trhex in hex_rect(*rect):  # noqa: F405
            self.assertEqual(hex_rect_index(*trhex,  # noqa: F405
                                            *rect), i)  # noqa: F405
            self.assertEqual(hex_rect_deindex(i,  # noqa: F405
                                              *rect), trhex)  # noqa: F405
            i += 1

        self.assertEqual(len(list(hex_rect(*rect))),  # noqa: F405
                         hex_rect_size(*rect))  # noqa: F405

    def test_hex_line_intersect(self):
        '''Test hex_line_intersect'''
        x1, y1 = hex_center(0, 0, 0)  # noqa: F405
        x2, y2 = hex_center(4, -3, -1)  # noqa: F405
        self.assertListEqual(list(hex_line_intersect(x1,   # noqa: F405
                                                     y1,
                                                     x2,
                                                     y2)), [  # noqa: F405
            (0, 0, 0),
            (1, -1, 0),
            (2, -1, -1),
            (2, -2, 0),
            (3, -2, -1),
            (4, -3, -1)
        ])

    def test_hex_line(self):
        '''Test hex_line'''
        self.assertListEqual(list(hex_line(0,  # noqa: F405
                                           0,
                                           0,
                                           4,
                                           -3,
                                           -1)), [
            (0, 0, 0),
            (1, -1, 0),
            (2, -1, -1),  # (2, -2, 0) would be an equally valid choice
            (3, -2, -1),
            (4, -3, -1)
        ])

    def test_hex_to_tris(self):
        '''Test hex_to_tris'''
        self.assertListEqual(hex_to_tris(1, 0, -1), [  # noqa: F405
            (2, 1, -2),
            (2, 2, -2),
            (1, 2, -2),
            (1, 2, -1),
            (1, 1, -1),
            (2, 1, -1),
        ])
        for tri in hex_to_tris(1, 0, -1):  # noqa: F405
            self.assertEqual(tri_to_hex(*tri), (1, 0, -1))  # noqa: F405

    def test_rect_intersect(self):
        '''Test hex_rect_intersect'''
        x1, y1 = tri_center(0, 1, 0)  # noqa: F405
        self.assertListEqual(list(hex_rect_intersect(x1,  # noqa: F405
                                                     y1,
                                                     0.6,
                                                     0.3)), [
            (0, 0, 0),
            (1, 0, -1),
            (0, 1, -1),
        ])

    def test_parent(self):
        '''Test hex_parent and hex_parent_center_child'''
        def test_parent(x, y, z, px, py, pz):
            c = (x, y, z)
            p = (px, py, pz)
            self.assertEqual(hex_parent(*c), p)  # noqa: F405
            self.assertEqual(hex_parent_center_child(*p), c)  # noqa: F405
            for n in hex_neighbours(*c):  # noqa: F405
                self.assertEqual(hex_parent(*n),  # noqa: F405
                                 p,
                                 f"{n} should have parent {p}")

        test_parent(0, 0, 0, 0, 0, 0)
        test_parent(5, -2, -3, 1, -1, 0)
        test_parent(3, -5, 2, 0, -1, 1)
        test_parent(-2, -3, 5, -1, 0, 1)
        test_parent(10, -4, -6, 2, -2, 0)


if __name__ == '__main__':
    unittest.main()
