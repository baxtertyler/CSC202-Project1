import unittest
from bears import *


# Starter test cases - write more!

class TestAssign1(unittest.TestCase):
    def test_bear_01(self):
        self.assertTrue(bears(250))

    def test_bear_02(self):
        self.assertTrue(bears(42))

    def test_bear_03(self):
        self.assertFalse(bears(53))

    def test_bear_04(self):
        self.assertFalse(bears(41))

    def test_bear_05(self):
        self.assertTrue(bears(84))

    def test_bear_06(self):
        self.assertTrue(bears(52))

    def test_bear_08(self):
        self.assertFalse(bears(0))

    def test_bear_09(self):
        self.assertFalse(bears(43))


if __name__ == "__main__":
    unittest.main()
