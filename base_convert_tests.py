import unittest
from base_convert import *


class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45, 2), "101101")
        self.assertEqual(convert(46, 2), "101110")
        self.assertEqual(convert(47, 2), "101111")

    def test_base4(self):
        self.assertEqual(convert(30, 4), "132")
        self.assertEqual(convert(31, 4), "133")
        self.assertEqual(convert(32, 4), "200")

    def test_base16(self):
        self.assertEqual(convert(314, 16), "13A")
        self.assertEqual(convert(315, 16), "13B")
        self.assertEqual(convert(316, 16), "13C")
        self.assertEqual(convert(317, 16), "13D")
        self.assertEqual(convert(318, 16), "13E")
        self.assertEqual(convert(319, 16), "13F")


if __name__ == "__main__":
    unittest.main()
