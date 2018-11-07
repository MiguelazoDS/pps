import random
import time
import MergeSort
import multiprocessing

#Recibe el objeto con las dos listas, el indice de proceso, y el tamaño de la lista del algoritmo
class Sensor(multiprocessing.Process):
    def __init__(self, obj, indice_lista,tamano):
        super(Sensor, self).__init__()
        self.obj=obj
        self.indice_lista=indice_lista
        self.tamano=tamano

    #Ejecuta la carga y luego guarda en el objeto el indice y el tiempo
    def run(self):
        inicio=time.time()
        while (1):
            MergeSort.mergesort([random.randint(0,self.tamano) for i in range(self.tamano)])
            self.obj.set_value(self.indice_lista, time.time())
