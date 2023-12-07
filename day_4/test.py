import unittest
import main as m

class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.part_one = m.PartOne('test_input_one.txt')

    def test_get_point_sum(self):
        sum = self.part_one.get_point_sum()

        self.assertEqual(sum, 13)

    def test_calculate_card_points(self):
        card_one = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'
        card_one_points = self.part_one.calculate_card_points(card_one)

        card_four = 'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83'
        card_four_points = self.part_one.calculate_card_points(card_four)

        card_six = 'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
        card_six_points = self.part_one.calculate_card_points(card_six)

        self.assertEqual(card_one_points, 8)
        self.assertEqual(card_four_points, 1)
        self.assertEqual(card_six_points, 0)

    def test_get_winning_numbers(self):
        card_one = self.part_one.get_winning_numbers('Card 1: 41 48 83 86 17')
        
        self.assertEqual(card_one, ['41', '48', '83', '86', '17'])

    def test_get_numbers_you_have(self):
        card_one = self.part_one.get_numbers_you_have('83 86  6 31 17  9 48 53')

        self.assertEqual(card_one, ['83', '86', '6', '31', '17', '9', '48', '53'])
        

class TestPartTwo(unittest.TestCase):
    pass
