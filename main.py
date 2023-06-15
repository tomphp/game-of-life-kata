import time
import random
import curses

from src.game import Game


# Function to initialize the game grid
def create_game(width, height) -> Game:
    return Game([[random.choice([0, 1]) for _ in range(width)] for _ in range(height)])


# Function to display the game grid
def display_grid(stdscr, game: Game):
    stdscr.clear()
    for row in game.grid:
        stdscr.addstr(''.join(['□' if cell else ' ' for cell in row]) + '\n')
    stdscr.refresh()


# Function to update the game grid based on the rules of the game
def update_grid(grid):
    pass


# Function to simulate the game of life
def simulate_game(stdscr, width, height, steps, interval):
    game = create_game(width, height)

    for _ in range(steps):
        display_grid(stdscr, game)
        game = game.update()
        time.sleep(interval)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use a breakpoint in the code line below to debug your script.
    # Initialize curses
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    # Example usage
    width = 50
    height = 20
    steps = 1000
    interval = 0.1

    simulate_game(stdscr, width, height, steps, interval)

    # Cleanup curses
    curses.echo()
    curses.nocbreak()
    curses.endwin()
