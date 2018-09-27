import random, multiprocessing
import time


class Sensor(multiprocessing.Process):

    def __init__(self, list, indice_lista):
        multiprocessing.Process.__init__(self)
        self.list=list
        self.indice_lista=indice_lista
        print(list)

    def run(self, list, indice_lista):
        while 1:
            print(list)
            time.sleep(random.randint(0,5))
            codigo_alarma = random.randint(0,10)
            print ( "Alarma en sensor",  str(indice_lista), str(codigo_alarma))
            self.list[indice_lista]=codigo_alarma
