from unittest import TestCase

from src.grid import *


class TestGrid(TestCase):
    def test_update_returns_dead_cell_when_all_neighbours_are_dead(self):
        g = Grid([
            [DEAD, DEAD, DEAD],
            [DEAD, DEAD, DEAD],
            [DEAD, DEAD, DEAD],
        ])

        resulting_grid = g.update()

        assert resulting_grid.matrix[1][1] == DEAD

    def test_update_returns_live_cell_when_two_neighbours_are_live(self):
        g = Grid([
            [DEAD, LIVE, DEAD],
            [DEAD, LIVE, DEAD],
            [DEAD, LIVE, DEAD],
        ])

        resulting_grid = g.update()

        assert resulting_grid.matrix[1][1] == LIVE

    def test_update_returns_dead_cell_north_neighbour_is_alive(self):
        g = Grid([
            [DEAD, LIVE, DEAD],
            [DEAD, LIVE, DEAD],
            [DEAD, DEAD, DEAD],
        ])

        resulting_grid = g.update()

        assert resulting_grid.matrix[1][1] == DEAD

    def test_update_returns_dead_cell_one_south_neighbour_is_alive(self):
        g = Grid([
            [DEAD, DEAD, DEAD],
            [DEAD, LIVE, DEAD],
            [DEAD, LIVE, DEAD],
        ])

        resulting_grid = g.update()

        assert resulting_grid.matrix[1][1] == DEAD

    def test_update_returns_live_cell_when_two_horizontal_neighbours_are_alive(self):
        g = Grid([
            [DEAD, DEAD, DEAD],
            [LIVE, LIVE, LIVE],
            [DEAD, DEAD, DEAD],
        ])

        resulting_grid = g.update()

        assert resulting_grid.matrix[1][1] == LIVE

    def test_update_returns_dead_cell_when_west_neighbours_are_alive(self):
        g = Grid([
            [DEAD, DEAD, DEAD],
            [LIVE, LIVE, DEAD],
            [DEAD, DEAD, DEAD],
        ])

        resulting_grid = g.update()

        assert resulting_grid.matrix[1][1] == DEAD

    def test_update_returns_dead_cell_when_east_neighbours_are_alive(self):
        g = Grid([
            [DEAD, DEAD, DEAD],
            [DEAD, LIVE, LIVE],
            [DEAD, DEAD, DEAD],
        ])

        resulting_grid = g.update()

        assert resulting_grid.matrix[1][1] == DEAD

    def test_update_returns_live_cell_when_north_and_east_neighbours_are_alive(self):
        g = Grid([
            [DEAD, LIVE, DEAD],
            [DEAD, LIVE, LIVE],
            [DEAD, DEAD, DEAD],
        ])

        resulting_grid = g.update()

        assert resulting_grid.matrix[1][1] == LIVE

    def test_update_returns_live_cell_when_north_and_northeast_neighbours_are_alive(self):
        g = Grid([
            [DEAD, LIVE, LIVE],
            [DEAD, LIVE, DEAD],
            [DEAD, DEAD, DEAD],
        ])

        resulting_grid = g.update()

        assert resulting_grid.matrix[1][1] == LIVE

    def test_live_cell_with_two_live_neighbours_stays_alive(self):
        test_cases = [
            [NORTH, SOUTH],
            [EAST, WEST],
            [NORTH, EAST],
            [EAST, SOUTH],
            [SOUTH, WEST],
            [WEST, NORTH],
            [NORTH, NORTH_EAST]
        ]
        for live_neighbours in test_cases:
            g = create_grid_with_live_neighbours(live_neighbours)
            resulting_grid = g.update()
            assert resulting_grid.matrix[1][1] == LIVE


def create_grid_with_live_neighbours(live_neighbours):
    a = [
        [DEAD, DEAD, DEAD],
        [DEAD, LIVE, DEAD],
        [DEAD, DEAD, DEAD],
    ]
    for row, col in live_neighbours:
        a[row][col] = LIVE
    g = Grid(a)
    return g
