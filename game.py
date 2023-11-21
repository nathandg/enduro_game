""" Enduro Game """
import curses
import time
from curses import wrapper

from elements.car import Car
from elements.enemy import Enemy
from scenario.Street import Street
from scenario.Sky import Sky
from scenario.Mountain import Mountain

from Player.PlayerInfo import PlayerInfo
from utils.Logger import Logger
from utils.Enums import Difficulty, TextEffects
from utils.Colors import Colors
from utils.ascii_art import winText
from utils.Score import Score


class Game():
    """ Classe principal do jogo """

    def __init__(self, stdscr):
        self.screen = stdscr
        self.main()

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

    def get_unique_name(self, width, height, colors):
        """ Get a unique name from the user """
        while True:
            self.screen.move(height//2 + 12, 0)
            self.screen.clrtoeol()
            self.write(
                width//2 - 15,
                height//2 + 12,
                "Nome já existe, digite outro: ",
                colors.ScoreText
            )
            name = self.screen.getstr().decode()
            if not Score.name_already_exists(name):
                return name

    def winGame(self, colors, width, height, time_elapsed):
        """ Win the game """
        self.draw(
            width//2 - len(winText[0])//2,
            height//2 - len(winText)//2,
            winText,
            colors.ScoreText)

        self.write(
            width//2 - 6,
            height//2 + 5,
            "Tempo: {:.2f}s".format(time_elapsed),
            colors.ScoreText,
            "BOLD")

        self.write(
            width//2 - 15,
            height//2 + 10,
            "Digite o seu nome: ",
            colors.ScoreText)

        curses.echo()
        self.screen.nodelay(False)
        self.screen.refresh()
        name = self.screen.getstr().decode()
        if Score.name_already_exists(name):
            name = self.get_unique_name(width, height, colors)
        Score.save_score(PlayerInfo.difficulty, time_elapsed, name)

    def main(self):
        """ main function """

        # Colors
        colors = Colors()

        # Curses config for game optimization
        curses.cbreak()
        curses.noecho()
        curses.curs_set(0)
        self.screen.keypad(True)
        self.screen.nodelay(True)

        # Screen Size
        height, width = self.screen.getmaxyx()
        Logger.log(
            "------- Iniciando o jogo {}x{} -------"
            .format(width, height))

        # Defina o FPS desejado
        FPS = 60
        frame_time_ms = int(1000.0 / FPS)

        gameCounter = 0
        enemyDistance = 0

        # Configurar a dificuldade
        Logger.log("Dificuldade: {}".format(PlayerInfo.difficulty))
        if (PlayerInfo.difficulty == Difficulty.NOOB):
            enemyDistance = 20
            PlayerInfo.position = 30
        elif (PlayerInfo.difficulty == Difficulty.EXPERT):
            enemyDistance = 12
            PlayerInfo.position = 60

        # Classes instances
        car = Car(width, height)
        street = Street(width, height)
        sky = Sky(width, height)
        mount_1 = Mountain(width, height, 10)
        mount_2 = Mountain(width, height, 120)
        adversaries = []

        started_time = time.time()

        # Game loop
        while True:
            if (PlayerInfo.position <= 0):
                time_elapsed = time.time() - started_time
                self.winGame(colors, width, height, time_elapsed)
                break

            gameCounter += 1
            key = self.screen.getch()

            actualStreet = street.update()
            car.update(key, actualStreet)
            colors.update(gameCounter)

            self.draw(0, 0, actualStreet, colors.street)
            self.draw(car.x, car.y, car.ascii, colors.playerCar)

            # Desenha o céu
            for i in range (5):
                self.draw(0, i, sky.skyBlock, colors.sky)

            # Desenha as montanhas
            for i in range(1, 5):
                mount_1.generate_mount(mount_1.initMount_x, mount_1.montanhaDistancia, i, street.state)
                mount_2.generate_mount(mount_2.initMount_x, mount_2.montanhaDistancia, i, street.state)

                offset = 7 - 3 * i

                x_position_1 = max(0, min(mount_1.initMount_x + offset, width - 1))
                x_position_2 = max(0, min(mount_2.initMount_x + offset, width - 1))

                self.draw(x_position_1, i, mount_1.montanhaCaracteres, colors.mountain)
                self.draw(x_position_2, i, mount_2.montanhaCaracteres, colors.mountain)

            # Cria os adversários
            if (len(adversaries) < 3 and gameCounter % enemyDistance == 0):
                adversaries.append(Enemy(width, height, colors.randomColor()))

            # Atualiza os adversários
            for enemy in adversaries:
                enemy.update(actualStreet)
                if(colors.isNight):
                    enemy.isNight = True
                    self.draw(enemy.x, enemy.y, enemy.ascii, 8)
                else:
                    enemy.isNight = False
                    self.draw(enemy.x, enemy.y, enemy.ascii, enemy.color)

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
            self.write(0, 6, "Posição: {}".format(
                PlayerInfo.position), colors.ScoreText)

            # Atualiza a tela
            self.screen.refresh()
            curses.napms(frame_time_ms)
