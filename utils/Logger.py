import time


class Logger():
    @staticmethod
    def clear():
        """ Clear file """
        with open("debug.txt", "w") as file:
            file.write(time.strftime("%d/%m/%Y %H:%M:%S")+"\n")
        file.close()

    @staticmethod
    def log(text):
        """ Write in file """
        with open("debug.txt", "a") as file:
            file.write(text + "\n")
        file.close()
