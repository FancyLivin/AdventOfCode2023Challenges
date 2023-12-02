import unittest
import main as m

class TestDayOne(unittest.TestCase):
    def setUp(self):
        self.day_one = m.DayOne('test_input.txt')
        self.assertIsNotNone(self.day_one.file)

    def test_calculate_sum(self):
        # real_int = 56049
        test_int = 142

        self.day_one.calculate_sum_of_strings()
        self.assertEqual(self.day_one.sum, test_int)

    def test_get_first_number(self):
        one = self.day_one.get_first_number('a1b2c3d4e5f')
        three = self.day_one.get_first_number('pqr3stu8vwx')

        self.assertEqual(one, 1)
        self.assertEqual(three, 3)

    def test_get_last_number(self):
        two = self.day_one.get_last_number('1abc2')
        seven = self.day_one.get_last_number('treb7uchet')

        self.assertEqual(seven, 7)
        self.assertEqual(two, 2)

class TestDayTwo(unittest.TestCase):
    pass