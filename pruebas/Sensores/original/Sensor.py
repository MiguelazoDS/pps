import random
import time
from multiprocessing import Process

class Sensor(Process):
    def __init__(self, obj, indice_lista):
        super(Sensor, self).__init__()
        self.obj=obj
        self.indice_lista=indice_lista

    def run(self):
        while 1:
            codigo_alarma = random.randint(0,10)
            time.sleep(random.randint(10,12))
            self.obj.set_value(self.indice_lista, codigo_alarma)
            print("Soy Sensor - Alarma - Lista", self.indice_lista, codigo_alarma, self.obj.get_obj())
