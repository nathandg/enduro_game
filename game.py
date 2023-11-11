""" Enduro Game """
import curses
from curses import wrapper

from elements.car import Car
from elements.enemy import Enemy
from scenario.Street import Street
from utils.Logger import Logger


class Game():
    """ Classe principal do jogo """

    def __init__(self):
        self.screen = None

    def draw(self, x, y, list, color=0):
        """ Print text in screen """
        for i, line in enumerate(list):
            self.screen.addstr(y + i, x, line, curses.color_pair(color))
        self.screen.refresh()

    def main(self, main_screen):
        """ main function """
        self.screen = main_screen

        # Curses config for game optimization
        napms_value = 25
        curses.cbreak()
        curses.noecho()
        curses.curs_set(0)
        main_screen.keypad(True)
        main_screen.nodelay(True)

        # Colors
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

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

        # Game loop
        while True:
            gameCounter += 1
            key = main_screen.getch()

            actualStreet = street.update()
            car.update(key, actualStreet)

            game.draw(0, 0, actualStreet)
            game.draw(car.x, car.y, car.ascii)

            # Cria os adversários
            if (len(adversaries) < 3 and gameCounter % 50 == 0):
                adversaries.append(Enemy(width, height))

            # Atualiza os adversários
            for enemy in adversaries:
                enemy.update(actualStreet)
                game.draw(enemy.x, enemy.y, enemy.ascii)

                if (enemy.yFinal >= height):
                    adversaries.remove(enemy)

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
