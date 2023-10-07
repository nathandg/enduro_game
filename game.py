""" Enduro Game """
import curses
from curses import wrapper

from car import Car
from ascii_art import title

class Game():
    """ Classe principal do jogo """

    def __init__(self):
        self.ascii_screen = []
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
        napms_value = 50
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
        self.make_safe_screen(width, height)
        
        # Classes instances
        car = Car(width, height)

        while True:
            key = main_screen.getch()
            car.update(key)

            game.draw(0, 0, self.ascii_screen)
            game.draw((width - len(title[0])) // 2, 10, title, 1)
            game.draw(car.x, car.y, car.ascii)

            # Atualize a tela
            main_screen.refresh()
            curses.napms(napms_value)
    
    def make_safe_screen(self, width, height):
        """ Make a safe screen """
        for i in range(height - 1):
            if i == 0 or i == height - 2:
                self.ascii_screen.append("-" * width)
            else:
                self.ascii_screen.append("|" + (" " * (width - 2)) + "|")
      
    def run(self):
        """ Run the game """
        wrapper(self.main)


if __name__ == "__main__":
    game = Game()
    game.run()