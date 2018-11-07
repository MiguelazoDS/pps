import random
import time
import MergeSort
import multiprocessing


class Sensor(multiprocessing.Process):
    def __init__(self, obj, indice_lista,tamano):
        super(Sensor, self).__init__()
        self.obj=obj
        self.indice_lista=indice_lista
        self.tamano=tamano

    def run(self):
        inicio=time.time()
        while (time.time()-inicio < 30):
            codigo_alarma = random.randint(0,10)
            MergeSort.mergesort([random.randint(0,self.tamano) for i in range(self.tamano)])
            tiempo = time.time()
            self.obj.set_value(self.indice_lista, tiempo)
