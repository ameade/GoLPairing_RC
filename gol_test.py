from gol import *
import unittest


class TestDeadOrAlive(unittest.TestCase):
    def test_dead_or_alive(self):
        # test middle dead
        world = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(0, dead_or_alive(world, 1, 1))

        # test middle alive
        world = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertEqual(1, dead_or_alive(world, 1, 1))

        # test wrap around left
        world = [[0, 0, 0], [0, 0, 1], [0, 0, 0]]
        self.assertEqual(1, dead_or_alive(world, 1, -1))

        # test wrap around right
        world = [[0, 0, 0], [1, 0, 0], [0, 0, 0]]
        self.assertEqual(1, dead_or_alive(world, 1, 3))

        # test wrap around up
        world = [[0, 0, 0], [0, 0, 0], [0, 1, 0]]
        self.assertEqual(1, dead_or_alive(world, -1, 1))

        # test wrap around right
        world = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(1, dead_or_alive(world, 3, 1))

        # test wrap around top and right
        world = [[0, 0, 0], [0, 0, 0], [1, 0, 0]]
        self.assertEqual(1, dead_or_alive(world, -1, 3))

class TestProgress(unittest.TestCase):
    def test_progress_world_empty_board(self):
        old_world = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected_new_world = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        actual_new_world = progress_world(old_world)
        self.assertListEqual(actual_new_world, expected_new_world)

class TestCountNeighbors(unittest.TestCase):
    def test_count_neighbors_zero(self):
        world = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(0, count_neighbors(world, 1, 1))

    def test_count_neighbors_one(self):
        world = [[0, 0, 0], [1, 0, 0], [0, 0, 0]]
        self.assertEqual(1, count_neighbors(world, 1, 1))

        # test wrapping on right edge
        world = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
        self.assertEqual(3, count_neighbors(world, 0, 2))

        # test dont count self
        world = [[1, 0, 1], [1, 0, 1], [1, 0, 1]]
        self.assertEqual(5, count_neighbors(world, 0, 2))

        world = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(8, count_neighbors(world, 1, 1))
