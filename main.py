""" Enduro Game """
import curses
from curses import wrapper
import time

title = [
    "······································································",
    ":███████╗███╗   ██╗██████╗ ██╗   ██╗██████╗  ██████╗                   :",
    ":██╔════╝████╗  ██║██╔══██╗██║   ██║██╔══██╗██╔═══██╗                  :",
    ":█████╗  ██╔██╗ ██║██║  ██║██║   ██║██████╔╝██║   ██║                  :",
    ":██╔══╝  ██║╚██╗██║██║  ██║██║   ██║██╔══██╗██║   ██║                  :",
    ":███████╗██║ ╚████║██████╔╝╚██████╔╝██║  ██║╚██████╔╝                  :",
    ":╚══════╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝                   :",
    ":                                                                      :",
    ": █████╗ ███████╗ ██████╗██╗██╗     ██████╗  █████╗ ███╗   ███╗███████╗:",
    ":██╔══██╗██╔════╝██╔════╝██║██║    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝:",
    ":███████║███████╗██║     ██║██║    ██║  ███╗███████║██╔████╔██║█████╗  :",
    ":██╔══██║╚════██║██║     ██║██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  :",
    ":██║  ██║███████║╚██████╗██║██║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗:",
    ":╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝:",
    "········································································",
]

car = [
    "  ______ ",
    " /|_||_\`.__ ",
    "(   _    _ _\ ",
    "=`-(_)--(_)-'",
]

wheel = [
    "|",
    "/",
    "-",
    "\\",
]


class Game():
    """ Game class """

    def __init__(self, screen):
        self.screen = screen

    def draw(self, x, y, list, color=0):
        """ Print text in screen """
        for i, line in enumerate(list):
            self.screen.addstr(y + i, x, line, curses.color_pair(color))
        self.screen.refresh()


def main(main_screen):
    """ main function """
    game = Game(main_screen)

    # Hide cursor
    curses.curs_set(0)

    # Init colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    x = 0
    wheel_idx = 0 

    while True:
        # clear screen
        main_screen.clear()

        # Print title
        game.draw(0, 0, title)

        # Print car
        game.draw(x, 15, car, 1)

        # Print wheels
        wheel_char = wheel[wheel_idx]
        game.draw(x + 4, 18, [wheel_char])
        game.draw(x + 9, 18, [wheel_char])

        # Update wheel index
        wheel_idx = (wheel_idx + 1) % len(wheel)

        # Update car position
        x = (x + 1) % (main_screen.getmaxyx()[1] - len(car[0]))

        # Refresh screen
        main_screen.refresh()
        time.sleep(0.1)

if __name__ == "__main__":
    wrapper(main)