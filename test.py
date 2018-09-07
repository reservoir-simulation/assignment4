#/usr/bin/env python

import unittest

from assignment4 import *

class TestSolution(unittest.TestCase):

    def test_pentadiagonal(self):

        assert pentadiagonal(2, 3) == [[2, -1, -1, 0, 0, 0],
                                      [-1, 2, 0, -1, 0, 0],
                                      [-1, 0, 3, -1, -1, 0],
                                      [0, -1, -1, 3, 0, -1],
                                      [0, 0, -1, 0, 2, -1],
                                      [0, 0, 0, -1, -1, 2]]


if __name__ == '__main__':
    unittest.main()
