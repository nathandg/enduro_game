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
        self.ScoreText = 6

        self.init_colors()

    def init_colors(self):
        for i, color in enumerate(self.pallet, start=1):
            curses.init_pair(i, color, curses.COLOR_BLACK)

    def dayTheme(self):
        for i, color in enumerate(self.pallet, start=1):
            curses.init_pair(i, color, curses.COLOR_BLACK)

        self.playerCar = 1
        self.street = 1
        self.ScoreText = 6

    def snowTheme(self):
        for i, color in enumerate(self.pallet, start=1):
            curses.init_pair(i, color, curses.COLOR_WHITE)

        self.playerCar = 8
        self.street = 8

    def nightTheme(self):
        for i, color in enumerate(self.pallet, start=2):
            curses.init_pair(i, curses.COLOR_BLACK, curses.COLOR_BLACK)

        self.playerCar = 1
        self.street = 1
        self.ScoreText = 1

    def randomColor(self):
        return random.randint(2, len(self.pallet) - 1)

    def update(self, gameCounter):
        if (gameCounter % 50 == 0):
            self.dayTheme()
            themes = [self.snowTheme, self.nightTheme, self.dayTheme]
            random.choice(themes)()
