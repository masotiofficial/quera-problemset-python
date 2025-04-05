import unittest

from calculator import calculate_floor


class TestFloorCalculation(unittest.TestCase):
    def test_sample_1(self):
        self.assertEqual(2, calculate_floor('UUUDU'))

    def test_sample_2(self):
        self.assertEqual(-4, calculate_floor('DDDD'))


if __name__ == '__main__':
    unittest.main()
