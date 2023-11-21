from utils.Enums import Direction


class Mountain():
    def __init__(self, width, height, initMount_x):
        self.width = width
        self.height = height
        self.initMount_x = initMount_x
        self.montanhaDistancia = 10
        self.montanhaCaracteres = []
        self.flag = False

    def generate_mount(self, inicio, distancia, altura, direction):
        eixoX = inicio + (distancia // altura * 2)
            
        caracteres = "█" * (altura * distancia)

        if direction == Direction.RIGHT:
            if 0 < self.initMount_x < self.width:
                self.initMount_x -= 1
            else:
                self.initMount_x = self.width - 1
        elif(direction == Direction.LEFT):
            if(eixoX < self.width and eixoX > 0):
                self.initMount_x = self.initMount_x +1
            else:
                self.initMount_x = 0

            
        self.montanhaCaracteres = [caracteres]