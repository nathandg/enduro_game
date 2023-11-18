import math
import random
from utils.Logger import Logger
from utils.Enums import Direction

DIRECTIONS = [Direction.LEFT, Direction.CENTER, Direction.RIGHT]


class Street():
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.CX = self.width / 2
        self.L = self.width * 0.65
        self.ascii = []

        self.counter = 0
        self.toMode = 100
        self.isMoving = False

        self.state = Direction.CENTER
        self.newState = None

        self.position = 0
        self.lenPositions = 0

        self.generate()

    def math(self, cx, y):
        y -= 8
        calc1 = cx + ((self.height - y) * (cx - self.CX) * y * 0.004)
        calc2 = ((self.L / (2 * self.height)) * y)

        esquerda = math.ceil(calc1 + calc2)
        direita = math.ceil(calc1 - calc2)

        if (esquerda < 0):
            esquerda = 1
        elif (direita < 0):
            direita = 1

        return esquerda, direita

    def generate(self):
        minCx = self.CX - (self.L * 0.1)
        maxCx = self.CX + (self.L * 0.1)
        positions = math.ceil(maxCx - minCx)
        Logger.log("Geração de pistas com o minCx {}.".format(minCx))
        for position in range(positions):
            Logger.log("Gerando a pista {} de {}.".format(
                position, round(self.L)))
            street = []
            for line in range(self.height):
                if(line > 7):
                    positionsX = self.math(minCx + position, line)
                    street.append(
                        " " * (self.width - positionsX[0] - 1)
                        + "|"
                        + " " * (positionsX[0] - positionsX[1] - 1)
                        + "|"
                        + " " * (positionsX[1] - 1))
                else:
                    street.append(
                    " " * (self.width - 1))

            self.ascii.append(street)
        self.lenPositions = len(self.ascii)
        self.position = self.lenPositions // 2

    def update(self):

        if self.isMoving:
            if self.state == Direction.LEFT:
                if self.newState == Direction.CENTER:
                    if self.position < self.lenPositions // 2:
                        self.position += 1
                    else:
                        self.isMoving = False
                        self.state = self.newState
                else:
                    if self.position < self.lenPositions - 1:
                        self.position += 1
                    else:
                        self.isMoving = False
                        self.state = self.newState

            elif self.state == Direction.CENTER:
                if self.newState == Direction.LEFT:
                    if self.position > 0:
                        self.position -= 1
                    else:
                        self.isMoving = False
                        self.state = self.newState
                else:
                    if self.position < self.lenPositions - 1:
                        self.position += 1
                    else:
                        self.isMoving = False
                        self.state = self.newState

            elif self.state == Direction.RIGHT:
                if self.newState == Direction.CENTER:
                    if self.position > self.lenPositions // 2:
                        self.position -= 1
                    else:
                        self.isMoving = False
                        self.state = self.newState
                else:
                    if self.position > 0:
                        self.position -= 1
                    else:
                        self.isMoving = False
                        self.state = self.newState

        self.counter += 1
        if self.counter >= self.toMode:
            self.newState = random.choice(DIRECTIONS)
            if self.newState != self.state:
                self.isMoving = True
                self.counter = 0
            else:
                self.counter = 80
        return self.ascii[self.position]
