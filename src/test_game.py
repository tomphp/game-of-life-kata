from unittest import TestCase
from testfixtures import compare

from src.game import Game


class TestGrid(TestCase):
    def test_update_returns_empty_grid_when_grid_empty(self):
        g = Game([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ])

        compare(g.update(), g)
