import os
import sys
import time
import random
import curses
from typing import List

from src.grid import Grid


# Function to display the game grid
def display_grid(stdscr, game: Grid):
    stdscr.clear()
    for y, row in enumerate(game.matrix):
        line = ''.join(['□ ' if cell else '  ' for cell in row])
        stdscr.addstr(y, 0, line)
    stdscr.refresh()


# Function to simulate the game of life
def run_game(stdscr, width, height, steps, interval):
    grid = Grid.initialize(width, height)

    for _ in range(steps):
        display_grid(stdscr, grid)
        grid = grid.update()
        time.sleep(interval)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use a breakpoint in the code line below to debug your script.
    # Initialize curses

    stdscr = curses.initscr()
    curses.noecho()
    # curses.cbreak()

    # Example usage
    width = 20
    height = 20
    steps = 1000
    interval = 1

    run_game(stdscr, 20, 20, 1000, 1)

    # Cleanup curses
    curses.echo()
    # curses.nocbreak()
    curses.endwin()
