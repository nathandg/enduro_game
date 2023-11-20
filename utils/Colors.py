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
        self.isNight = False

        # Elements Colors
        self.playerCar = 1
        self.street = 1
        self.ScoreText = 6
        self.sky = 2
        self.mountain = 4

        self.init_colors()
        self.dayTheme()

    def init_colors(self):
        for i, color in enumerate(self.pallet, start=1):
            curses.init_pair(i, color, curses.COLOR_BLACK)

    def dayTheme(self):
        for i, color in enumerate(self.pallet, start=1):
            curses.init_pair(i, color, curses.COLOR_GREEN)

        self.playerCar = 1
        self.street = 1
        self.ScoreText = 1
        self.sky = 2
        self.mountain = 4
        self.isNight = False


    def snowTheme(self):
        for i, color in enumerate(self.pallet, start=1):
            curses.init_pair(i, color, curses.COLOR_WHITE)

        self.playerCar = 8
        self.street = 8
        self.ScoreText = 8
        self.sky = 2
        self.mountain = 1
        self.isNight = False


    def nightTheme(self):
        for i, color in enumerate(self.pallet, start=1):
            curses.init_pair(i, color, curses.COLOR_BLACK)

        self.street = 1
        self.playerCar = 1
        self.ScoreText = 1
        self.sky = 8
        self.mountain = 1
        self.isNight = True

    def randomColor(self):
        return random.choice([3, 7, 5])
    
    def update(self, gameCounter):
        if (gameCounter % 50 == 0):
            themes = [self.dayTheme, self.snowTheme, self.nightTheme]
            random.choice(themes)()
