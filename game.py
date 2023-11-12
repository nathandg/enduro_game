""" Enduro Game """
import curses
from curses import wrapper

from elements.car import Car
from elements.enemy import Enemy
from scenario.Street import Street

from utils.Logger import Logger
from Player.PlayerInfo import PlayerInfo
from utils.Enums import Difficulty, TextEffects
from utils.Colors import Colors


class Game():
    """ Classe principal do jogo """

    def __init__(self):
        self.screen = None

    def draw(self, x, y, list, color=1, effect=None):
        """ Print text in screen """
        for i, line in enumerate(list):
            self.write(x, y + i, line, color, effect)

    def write(self, x, y, text, color, effect=None):
        """ Print text in screen """
        if effect and effect in TextEffects.__members__:
            combined = curses.color_pair(color) | TextEffects[effect].value
            self.screen.addstr(y, x, text, combined)  
        else:
            self.screen.addstr(y, x, text, curses.color_pair(color))

    def main(self, main_screen):
        """ main function """
        self.screen = main_screen

        # Colors
        colors = Colors()

        # Curses config for game optimization
        napms_value = 25
        curses.cbreak()
        curses.noecho()
        curses.curs_set(0)
        main_screen.keypad(True)
        main_screen.nodelay(True)

        # Screen Size
        height, width = main_screen.getmaxyx()
        Logger.log(
            "------- Iniciando o jogo {}x{} -------"
            .format(width, height))

        # Classes instances
        car = Car(width, height)
        street = Street(width, height)
        adversaries = []

        gameCounter = 0

        # Configurar a dificuldade
        PlayerInfo.difficulty = Difficulty.NOOB
        if (PlayerInfo.difficulty == Difficulty.NOOB):
            PlayerInfo.position = 30
        elif (PlayerInfo.difficulty == Difficulty.EXPERT):
            PlayerInfo.position = 50

        # Game loop
        while True:
            if PlayerInfo.position <= 20:
                colors.snowTheme()
            if PlayerInfo.position <= 0:
                break

            gameCounter += 1
            key = main_screen.getch()

            actualStreet = street.update()
            car.update(key, actualStreet)

            game.draw(0, 0, actualStreet, colors.street)
            game.draw(car.x, car.y, car.ascii, colors.playerCar)

            # Cria os adversários
            if (len(adversaries) < 3 and gameCounter % 50 == 0):
                adversaries.append(Enemy(width, height, colors.randomColor()))

            # Atualiza os adversários
            for enemy in adversaries:
                enemy.update(actualStreet)
                game.draw(enemy.x, enemy.y, enemy.ascii, enemy.color)
                if (enemy.yFinal >= height):
                    PlayerInfo.overtake()
                    adversaries.remove(enemy)

            # Mostra as informações do jogador
            game.write(0, 1, "Posição: {}".format(PlayerInfo.position), 6)

            # Atualiza a tela
            main_screen.refresh()
            curses.napms(napms_value)

    def run(self):
        """ Run the game """
        wrapper(self.main)


if __name__ == "__main__":
    Logger.clear()
    game = Game()
    game.run()
