class Score():

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

    @staticmethod
    def name_already_exists(name):
        """ Validate if name already exists """
        saves = Score.load_scores()
        for save in saves:
            if name == save.split(",")[2].strip():
                return True
        return False
