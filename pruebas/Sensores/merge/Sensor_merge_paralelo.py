import random
import time
import MergeSort
from multiprocessing import Process


class Sensor(Process):
    def __init__(self, obj, indice_lista,tamano):
        super(Sensor, self).__init__()
        self.obj=obj
        self.indice_lista=indice_lista
        self.tamano=tamano

    def run(self):
        while 1:
            codigo_alarma = random.randint(0,10)
            MergeSort.mergesort_paralelo([random.randint(0,self.tamano) for i in range(self.tamano)])
            tiempo = time.time()
            self.obj.set_value(self.indice_lista, tiempo)
            #print("Soy Sensor - Alarma - Lista", self.indice_lista, codigo_alarma, self.obj.get_obj())
