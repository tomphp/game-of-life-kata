from typing import List

import numpy as np


class Grid:
    matrix: List[List[int]]

    @staticmethod
    def initialize(width, height):
        return Grid(np.random.randint(2, size=(width, height)).tolist())

    def __init__(self, matrix: List[List[int]]) -> None:
        self.matrix = matrix

    def update(self):
        newgrid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        return Grid(newgrid)

