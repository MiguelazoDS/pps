import random
import time
import process_queue_3
from multiprocessing import Process

class Sensor(Process):
    def __init__(self, obj, indice_lista, tamano):
        super(Sensor, self).__init__()
        self.obj=obj
        self.indice_lista=indice_lista
        self.tamano = tamano

    def run(self):
        while 1:
            process_queue_3.main(self.tamano)
            tiempo_actual = time.time()
            self.obj.set_value(self.indice_lista, tiempo_actual)
#            print("Soy Sensor - Alarma - Lista", self.indice_lista, tiempo_actual, self.obj.get_obj())
