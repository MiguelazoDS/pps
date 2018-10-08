import random
import time
import MergeSort
from multiprocessing import Process

N = 100

class Sensor(Process):
    def __init__(self, obj, indice_lista):
        super(Sensor, self).__init__()
        self.obj=obj
        self.indice_lista=indice_lista

    def run(self):
        while 1:
            codigo_alarma = random.randint(0,10)
            #time.sleep(random.randint(10,12))
            MergeSort.mergesort_paralelo([random.randint(0,N) for i in range(N)])
            self.obj.set_value(self.indice_lista, codigo_alarma)
            print("Soy Sensor - Alarma - Lista", self.indice_lista, codigo_alarma, self.obj.get_obj())
