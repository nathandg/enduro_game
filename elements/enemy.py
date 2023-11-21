import random

from utils.ascii_art import enemy_art_bg, enemy_art_md, enemy_art_sm, enemy_art_bg_night, enemy_art_md_night, enemy_art_sm_night
from utils.Logger import Logger
from utils.Enums import Difficulty
from Player.PlayerInfo import PlayerInfo


class Enemy:
    def __init__(self,  screenWidth, screenHeight, color=1):
        self.isNight = False
        self.ascii = enemy_art_sm
        self.width = screenWidth
        self.height = screenHeight
        self.carWidth = len(self.ascii[1])
        self.carHeight = len(self.ascii)

        self.x = (self.width - len(self.ascii[0])) // 2
        self.y = 10
        self.xFinal = self.x + self.carWidth
        self.yFinal = self.y + self.carHeight

        self.increment = 0
        self.incrementToMove = self.getIncrementByDifficulty()
        self.borderDistance = 5
        self.borderChoice = random.choice(["left", "right"])
        self.color = color

    def getIncrementByDifficulty(self):
        if PlayerInfo.difficulty == Difficulty.NOOB:
            return 2
        elif PlayerInfo.difficulty == Difficulty.EXPERT:
            return 0

    def identifyPositions(self, street):
        # TODO: Refatorar
        positions = []

        i = 0
        while i < len(street):
            if street[i] == "▐":
                positions.append(i)
            i += 1

        if self.borderChoice == "left":
            return positions[0]
        else:
            return positions[1]
        # return self.width // 2

    def changeCarSize(self, size):
        if size == "big":
            if(self.isNight):
                self.ascii = enemy_art_bg_night
            else:
                self.ascii = enemy_art_bg
        elif size == "medium":
            if(self.isNight):
                self.ascii = enemy_art_md_night
            else:
                self.ascii = enemy_art_md
        else:
            if(self.isNight):
                self.ascii = enemy_art_sm_night
            else:
                self.ascii = enemy_art_sm

        self.carWidth = len(self.ascii[0])
        self.carHeight = len(self.ascii)
        self.xFinal = self.x + self.carWidth
        self.yFinal = self.y + self.carHeight

    def collide(self, car):
        if self.borderChoice == "left":
            return self.xFinal > car.x
        else:
            Logger.log("Enemy right: x: {} | car.xFinal: {}".format(
                self.x, car.xFinal))
            return self.x < car.xFinal

    def update(self, street):
        complete = self.y / self.height * 100

        newPosition = self.identifyPositions(street[self.y])

        if self.borderChoice == 'left':
            self.x = newPosition + self.borderDistance
        else:
            self.x = newPosition - self.borderDistance - self.carWidth

        # Atualiza o tamanho do desenho
        if complete >= 60:
            self.changeCarSize("big")
        elif complete >= 30:
            self.changeCarSize("medium")
        else:
            self.changeCarSize("small")

        if (self.increment >= self.incrementToMove):
            self.increment = 0
            self.y += 1
            self.yFinal += 1
        else:
            self.increment += 1
