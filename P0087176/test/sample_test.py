import unittest
from ..source import game


class Test(unittest.TestCase):

    def test_sample_1(self):
        self.assertEqual(str(game(17)), str(6))

    def test_sample_2(self):
        self.assertEqual(str(game(81)), str(7))


if __name__ == '__main__':
    unittest.main()
