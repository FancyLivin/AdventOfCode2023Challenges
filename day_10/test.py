import unittest
import main as m

class TestPartOne(unittest.TestCase):
    def setUp(self) -> None:
        self.one = m.PartOne('test_one.txt')

    def test_get_start_coords(self):
        self.assertEqual(self.one.start, (1, 1))
    
    # @unittest.skip
    def test_get_farthest_point(self):
        # farthest = self.one.get_farthest_point()
        # self.assertEqual(farthest, 4)

        two = m.PartOne('test_two.txt')
        farthest = two.get_farthest_point()
        self.assertEqual(farthest, 8)
        # fails when going from (2,4) to (3,3) instead goes to (1,5)
    
    @unittest.skip
    def test_move_cardinal_directions(self):
        coords = self.one.change_coordinates('N', (1,1), (-1,-1), '|')
        self.assertEqual(coords[0], (3, 1))

        coords = self.one.change_coordinates('W', (3,1), (1,1), '-')
        self.assertEqual(coords[0], (3, 3))

        coords = self.one.change_coordinates('S', (3,3), (3,1), '|')
        self.assertEqual(coords[0], (1, 3))

        coords = self.one.change_coordinates('E', (1,3), (3,3), '-')
        self.assertEqual(coords[0], (1, 1))

    @unittest.skip
    def test_move_around_corners(self):
        coords = self.one.change_coordinates('N', (1,2), (-1,-1), 'L')
        self.assertEqual(coords[0], (2,3))

class TestPartTwo(unittest.TestCase):
    pass
