import unittest
from maze import Maze



class Tests(unittest.TestCase):
    def setUp(self):
        self.win = None

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=self.win)
        self.assertEqual(len(m1._cell), num_cols)
        self.assertEqual(len(m1._cell[0]), num_rows)

    def test_maze_create_cells_2(self):
        num_cols = 20
        num_rows = 120
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20, win=self.win)
        self.assertEqual(len(m1._cell), num_cols)
        self.assertEqual(len(m1._cell[0]), num_rows)

    # test with negative values
    def test_maze_create_cells_3(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, -20, 20, win=self.win)
        self.assertEqual(len(m1._cell), num_cols)
        self.assertEqual(len(m1._cell[0]), num_rows)

    def test_entrance_creation(self):
        # Test that the top wall of the top-left cell is broken
        m1 = Maze(0, 0, 1, 1, 10, 10, win=self.win)
        m1._break_entrance_and_exit()
        self.assertFalse(m1._cell[0][0].has_top_wall)

    def test_exit_creation(self):
        # Test that the bottom wall of the bottom-right cell is broken
        m1 = Maze(0, 0, 1, 1, 10, 10, win=self.win)
        m1._break_entrance_and_exit()
        self.assertFalse(m1._cell[0][0].has_bottom_wall)

    def test_other_walls_intact(self):
        # Test that the other walls of the top-left cell are intact
        m1 = Maze(0, 0, 3, 3, 10, 10, win=self.win)
        m1._break_entrance_and_exit()
        entrance_cell = m1._cell[0][0]
        exit_cell = m1._cell[2][2]
        self.assertTrue(entrance_cell.has_right_wall)
        self.assertTrue(entrance_cell.has_bottom_wall)
        self.assertTrue(entrance_cell.has_left_wall)
        self.assertTrue(exit_cell.has_left_wall)
        self.assertTrue(exit_cell.has_right_wall)
        self.assertTrue(exit_cell.has_top_wall)

    def test_cell_visit_resetting(self):
        m1 = Maze(0, 0, 3, 3, 10, 10, win=self.win)
        m1._reset_cells_visited()
        for i in range(3):
            for j in range(3):
                self.assertFalse(m1._cell[i][j].visited)
    


if __name__ == '__main__':
    unittest.main()