import math
from utils.Logger import Logger


class Street():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.CX = self.width / 2
        self.L = self.width * 0.65
        self.ascii = []
        self.generate()

    def math(self, cx, y):
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
            Logger.log("Gerando a pista {} de {}.".format(position, round(self.L)))
            street = []
            for line in range(self.height):
                positionsX = self.math(minCx + position, line)
                street.append(
                    " " * (self.width - positionsX[0] - 1)
                    + "|"
                    + " " * (positionsX[0] - positionsX[1] - 1)
                    + "|"
                    + " " * (positionsX[1] - 1))
            self.ascii.append(street)


if __name__ == "__main__":
    street = Street()
    screen = []

    for i in range(street.height):
        print(street.math(150, i))
        print("-----------\n")
