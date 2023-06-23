from typing import List

import numpy as np

DEAD = 0
LIVE = 1

NORTH = (0, 1)
NORTH_EAST = (0,2)
EAST = (1, 2)
SOUTH = (2, 1)
WEST = (1, 0)


class Grid:
    matrix: List[List[int]]

    @staticmethod
    def initialize(width, height):
        return Grid(np.random.randint(2, size=(width, height)).tolist())

    def __init__(self, matrix: List[List[int]]) -> None:
        self.matrix = matrix

    def update(self):
        number_of_live_neighbours = self._count_live_neighbours()

        if number_of_live_neighbours == 2:
            return Grid([[DEAD, DEAD],
                         [DEAD, LIVE]])

        return Grid([[DEAD, DEAD],
                     [DEAD, DEAD]])

    def _count_live_neighbours(self):
        neighbours = [NORTH, NORTH_EAST, SOUTH, EAST, WEST]
        neighbour_states = [self.matrix[row][column] for row, column in neighbours]
        number_of_live_neighbours = len([state for state in neighbour_states if state == LIVE])
        return number_of_live_neighbours
