import curses
import random


class Colors():
    def __init__(self):
        curses.start_color()
        self.pallet = [
            curses.COLOR_WHITE,
            curses.COLOR_CYAN,
            curses.COLOR_RED,
            curses.COLOR_YELLOW,
            curses.COLOR_BLUE,
            curses.COLOR_GREEN,
            curses.COLOR_MAGENTA,
            curses.COLOR_BLACK
        ]

        # Elements Colors
        self.playerCar = 1
        self.street = 1
        self.ScoreText = 1

        self.init_colors()

    def init_colors(self):
        for i, color in enumerate(self.pallet, start=1):
            curses.init_pair(i, color, curses.COLOR_BLACK)

    def snowTheme(self):
        for i, color in enumerate(self.pallet, start=1):
            curses.init_pair(i, color, curses.COLOR_WHITE)

        self.playerCar = 8
        self.street = 8

    def randomColor(self):
        return random.randint(2, len(self.pallet) - 1)
