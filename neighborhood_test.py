import unittest
from Neighborhood import Neighborhood


class TestNeighborhood(unittest.TestCase):

    def test_example_1(self):
        n = Neighborhood(3, 11, 11, [(5, 5)])
        self.assertEqual(n.solve(), 25)

    def test_example_2(self):
        n = Neighborhood(3, 11, 11, [(5, 1)])
        self.assertEqual(n.solve(), 21)

    def test_example_3(self):
        n = Neighborhood(n=2, h=11, w=11, filled_cells=[(7, 7), (3, 3)])
        self.assertEqual(n.solve(), 26)

    def test_example_4(self):
        n = Neighborhood(n=2, h=11, w=11, filled_cells=[(3, 3), (4, 5)])
        self.assertEqual(n.solve(), 22)

    def test_overlap_and_runoff(self):
        n = Neighborhood(n=2, h=11, w=11, filled_cells=[(1, 3), (3, 1)])
        self.assertEqual(n.solve(), 21)

    def test_adjacent_positives(self):
        n = Neighborhood(n=2, h=11, w=11, filled_cells=[
                         (5, 5), (5, 4), (5, 6)])
        self.assertEqual(n.solve(), 23)

    def test_corners(self):
        n = Neighborhood(n=2, h=11, w=11, filled_cells=[
                         (0, 0), (10, 0), (0, 10), (10, 10)])
        self.assertEqual(n.solve(), 24)

    def test_minimum_array_empty(self):
        n = Neighborhood(n=1, h=1, w=1, filled_cells=[])
        self.assertEqual(n.solve(), 0)

    def test_minimum_array_full(self):
        n = Neighborhood(n=1, h=1, w=1, filled_cells=[(0, 0)])
        self.assertEqual(n.solve(), 1)

    def test_n_is_zero(self):
        n = Neighborhood(n=0, h=11, w=11, filled_cells=[
                         (0, 0), (2, 2), (3, 3)])
        self.assertEqual(n.solve(), 3)

    def test_one_row(self):
        n = Neighborhood(n=2, h=1, w=11, filled_cells=[(0, 5)])
        self.assertEqual(n.solve(), 5)

    def test_one_col(self):
        n = Neighborhood(n=2, h=11, w=1, filled_cells=[(5, 0)])
        self.assertEqual(n.solve(), 5)

    def test_large_n_large_sparse_board(self):
        n = Neighborhood(n=10000000000, h=1000, w=1000,
                         filled_cells=[(500, 500)])
        self.assertEqual(n.solve(), 1000000)

    def test_large_n_filled_board(self):
        size = 30
        n = Neighborhood(n=10000000, h=size, w=size, filled_cells=[
                         (x, y) for x in range(size) for y in range(size)])
        self.assertEqual(n.solve(), size*size)

    def test_corner_cutoff_large_n(self):
        n = Neighborhood(n=100000, h=2, w=1000, filled_cells=[(0, 0)])
        self.assertEqual(n.solve(), 2000)


if __name__ == '__main__':
    unittest.main()
