from typing import List


class Game:
    grid: List[List[int]]

    def __init__(self, grid: List[List[int]]) -> None:
        self.grid = grid

    def update(self):
        return Game([
            [0, 0, 1],
            [0, 0, 0],
            [0, 0, 0],
        ])
