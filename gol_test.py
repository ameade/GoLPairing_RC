from gol import *
import unittest

class TestProgressBoard(unittest.TestCase):
    def test_progress_board_empty(self):
        old_board = [[False, False, False],
                     [False, False, False],
                     [False, False, False],]

        expected_board = [[False, False, False],
                          [False, False, False],
                          [False, False, False]]

        actual_board = progress_board(old_board)
        self.assertEqual(actual_board, expected_board)

    def test_progress_board_one_cell(self):
        """ Tests that a single cell in the middle dies, based on rule 1 """
        old_board = [[False, False, False],
                     [False, True, False],
                     [False, False, False]]

        expected_board = [[False, False, False],
                          [False, False, False],
                          [False, False, False]]

        actual_board = progress_board(old_board)
        self.assertEqual(actual_board, expected_board)

    def test_count_neighbors_zero(self):
        board = [[False, False, False],
                 [False, True, False],
                 [False, False, False]]
        self.assertEqual(0, count_neighbors(board, 1, 1))

    def test_count_neighbors_one(self):
        board = [[False, False, False],
                 [False, True, True],
                 [False, False, False]]
        self.assertEqual(1, count_neighbors(board, 1, 1))

    def test_count_neighbors_4by3(self):
        board = [[False, False, False, True],
                 [False, True, True, True],
                 [False, False, False, True]]
        self.assertEqual(1, count_neighbors(board, 1, 1))
    
    def test_count_neighbors_4by3(self):
        board = [[False, False, False, True],
                 [False, True, True, True],
                 [False, False, False, True],
                 [False, True, True, True],
                 [False, True, True, True],
                 [False, False, False, True]]
        self.assertEqual(1, count_neighbors(board, 1, 1))

    def test_get_neighborhood(self):
        board = [[False, False, False, True],
                 [False, True, True, True],
                 [False, False, False, True],
                 [False, True, True, True],
                 [False, True, True, True],
                 [False, False, False, True]]
        row = 1
        col = 1
        neighborhood = [[False, False, False],
                        [False, True, True],
                        [False, False, False]]
        self.assertEqual(neighborhood, get_neighborhood(board, row, col))