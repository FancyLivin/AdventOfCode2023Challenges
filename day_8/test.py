import unittest
import main as m

class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.one = m.PartOne('test_two.txt')

    def test_directions(self):
        self.assertEqual(self.one.directions, 'LLR')

    def test_get_network(self):
        dictionary = {
            'AAA' : ('BBB', 'BBB'),
            'BBB' : ('AAA', 'ZZZ'),
            'ZZZ' : ('ZZZ', 'ZZZ')
        }

        self.assertEqual(self.one.network, dictionary)

    def test_find_total_steps(self):
        self.assertEqual(self.one.steps, 6)

class TestPartTwo(unittest.TestCase):
    pass
