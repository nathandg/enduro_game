""" Enduro Game """
import curses
import random
import time
from curses import wrapper

from elements.car import Car
from elements.enemy import Enemy
from scenario.Street import Street

from Player.PlayerInfo import PlayerInfo
from utils.Logger import Logger
from utils.Enums import Difficulty, TextEffects
from utils.Colors import Colors
from utils.ascii_art import winText
from utils.Score import Score


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

    def get_unique_name(self, main_screen, width, height, colors):
        """ Get a unique name from the user """
        while True:
            main_screen.move(height//2 + 12, 0)
            main_screen.clrtoeol()
            game.write(
                width//2 - 15,
                height//2 + 12,
                "Nome já existe, digite outro: ",
                colors.ScoreText
            )
            name = main_screen.getstr().decode()
            if not Score.name_already_exists(name):
                return name

    def winGame(self, main_screen, colors, width, height, time_elapsed):
        """ Win the game """
        game.draw(
            width//2 - len(winText[0])//2,
            height//2 - len(winText)//2,
            winText,
            colors.ScoreText)

        game.write(
            width//2 - 6,
            height//2 + 5,
            "Tempo: {:.2f}s".format(time_elapsed),
            colors.ScoreText,
            "BOLD")

        game.write(
            width//2 - 15,
            height//2 + 10,
            "Digite o seu nome: ",
            colors.ScoreText)

        main_screen.nodelay(False)
        curses.echo()
        main_screen.refresh()
        name = main_screen.getstr().decode()
        if Score.name_already_exists(name):
            name = self.get_unique_name(main_screen, width, height, colors)
        Score.save_score(PlayerInfo.difficulty, time_elapsed, name)

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

        gameCounter = 0
        enemyDistance = 0

        # Configurar a dificuldade
        PlayerInfo.difficulty = Difficulty.NOOB
        if (PlayerInfo.difficulty == Difficulty.NOOB):
            enemyDistance = 20
            PlayerInfo.position = 30
        elif (PlayerInfo.difficulty == Difficulty.EXPERT):
            enemyDistance = 10
            PlayerInfo.position = 60

        # Classes instances
        car = Car(width, height)
        street = Street(width, height)
        adversaries = []

        started_time = time.time()

        # Game loop
        while True:
            if (PlayerInfo.position <= 0):
                time_elapsed = time.time() - started_time
                self.winGame(main_screen, colors, width, height, time_elapsed)
                break

            gameCounter += 1
            key = main_screen.getch()

            actualStreet = street.update()
            car.update(key, actualStreet)
            colors.update(gameCounter)

            game.draw(0, 0, actualStreet, colors.street)
            game.draw(car.x, car.y, car.ascii, colors.playerCar)

            # Cria os adversários
            if (len(adversaries) < 3 and gameCounter % enemyDistance == 0):
                adversaries.append(Enemy(width, height, colors.randomColor()))

            # Atualiza os adversários
            for enemy in adversaries:
                enemy.update(actualStreet)
                game.draw(enemy.x, enemy.y, enemy.ascii, enemy.color)

                if car.y < (enemy.yFinal-4) and enemy.collide(car):
                    Logger.log("Crash!")
                    curses.beep()
                    curses.flash()
                    PlayerInfo.crash()
                    adversaries.remove(enemy)

                elif enemy.yFinal >= height:
                    PlayerInfo.overtake()
                    adversaries.remove(enemy)

            # Mostra as informações do jogador
            game.write(0, 1, "Posição: {}".format(
                PlayerInfo.position), colors.ScoreText)

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
