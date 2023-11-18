
class PlayerInfo:
    position = 0
    difficulty = 0

    @staticmethod
    def overtake():
        PlayerInfo.position -= 1

    @staticmethod
    def crash():
        PlayerInfo.position += 1
