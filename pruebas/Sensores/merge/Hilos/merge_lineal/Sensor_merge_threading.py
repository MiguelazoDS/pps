import random
import time
import MergeSort
import threading

class Sensor(threading.Thread):
    def __init__(self, lista, indice_lista,tamano):
        super(Sensor, self).__init__()
        self.lista=lista
        self.indice_lista=indice_lista
        self.tamano=tamano

    def run(self):
        inicio=time.time()
        while(time.time()-inicio < 5):
            MergeSort.mergesort([random.randint(0,self.tamano) for i in range(self.tamano)])
            self.lista[self.indice_lista]=time.time()
