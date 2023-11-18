import curses
from enum import Enum


class Difficulty(Enum):
    NOOB = 0
    EXPERT = 1


class Direction(Enum):
    LEFT = 0
    CENTER = 1
    RIGHT = 2


class TextEffects(Enum):
    BOLD = curses.A_BOLD
    BLINK = curses.A_BLINK
    UNDERLINE = curses.A_UNDERLINE
