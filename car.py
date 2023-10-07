import curses
from ascii_art import car_art

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
    
    def update(self, key):
        if key == curses.KEY_RIGHT:
            self.direction = "right"
                        
        elif key == curses.KEY_LEFT:
            self.direction = "left"
        
        # elif key != curses.KEY_RIGHT and key != curses.KEY_LEFT:
        #     self.direction = "parado"

        if self.direction == "right":
            self.x += 1

        elif self.direction == "left":
            self.x -= 1
      