class Score():

    @staticmethod
    def create_file():
        """ Create file if not exists """
        try:
            with open("scores.csv", "r") as file:
                file.close()
        except FileNotFoundError:
            with open("scores.csv", "w") as file:
                file.write("Difficulty, Time, Name \n")
            file.close()

    @staticmethod
    def save_score(difficulty, time, name):
        """ Clear file """
        with open("scores.csv", "a") as file:
            file.write("{}, {}, {} \n".format(difficulty, time, name))
        file.close()

    @staticmethod
    def load_scores():
        """ Load scores from file """
        scores = []
        with open("scores.csv", "r") as file:
            for line in file:
                scores.append(line)
        file.close()
        return scores
