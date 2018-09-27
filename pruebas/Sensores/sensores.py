import random, multiprocesing

class sensor(multiprocesing.process):
    def __init__(self, list):
        multiprocesing.process.__init__(self)
        self.list=list
    def run(self):
        while 1:
            sleep(randint(0,5))


def sensores():
    sleep(randint(0,5))
    return


def main():
    sensores[]


if __name__ == '__main__':
    main()
