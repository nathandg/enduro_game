import curses
from utils.ascii_art import car_art
from utils.Logger import Logger


class Car:
    def __init__(self,  width, height):
        self.ascii = car_art
        self.width = width
        self.height = height
        self.x = (self.width - len(self.ascii[0])) // 2
        self.y = self.height - len(self.ascii) - 1
        self.xFinal = self.x + len(self.ascii[0])
        self.yFinal = self.y + len(self.ascii)
        self.direction = ""

    def checkCollisionWithBorder(self, street):
        Logger.log("\n\n ------ Car Check Collision -----")
        positions = []
        for i, x in enumerate(street):
            if x == "|":
                positions.append(i)

        if self.x <= positions[0]:
            self.x = positions[0]
            return 'left-block'
        elif self.x >= (positions[1] - len(self.ascii[0])):
            self.x = positions[1] - len(self.ascii[0])
            return 'right-block'

        return False

    def update(self, key, street):
        collided = self.checkCollisionWithBorder(street[self.y])

        if collided == 'left-block':
            if key == curses.KEY_RIGHT:
                self.direction = "right"
            else:
                self.direction = "blocked"

        elif collided == 'right-block':
            if key == curses.KEY_LEFT:
                self.direction = "left"
            else:
                self.direction = "blocked"

        elif key == curses.KEY_RIGHT:
            self.direction = "right"

        elif key == curses.KEY_LEFT:
            self.direction = "left"

        if self.direction == "right":
            self.x += 3

        elif self.direction == "left":
            self.x -= 3
