import Sensor_merge_lineal
import random
import time
from multiprocessing import Process, Manager, Lock
from multiprocessing.managers import BaseManager


def alarmas(object, num_process):
    inicio=time.time()
    while (time.time()-inicio < 30):
            lista = object.get_obj()
            for i in range (0,num_process):
                if(lista[i]>0):
                    tiempo = time.time() - lista[i]
                    object.set_value(i,-1)
                    print (tiempo)


class ListObj(object):
        def __init__(self, lista):
                self.lista = lista

        def set_value(self, indice_lista, tiempo_atencion):
                self.lista[indice_lista] = tiempo_atencion

        def get_obj(self):
                return self.lista


if __name__=="__main__":

        BaseManager.register('ListObj', ListObj)
        manager = BaseManager()
        manager.start()

        num_process = 15 #cantidad de senores
        tamano = 100000

        lista=list(range(num_process))
        lista = [-1 for i in range(num_process)] #inicializamos con -1
        listObl = manager.ListObj(lista)

        print(listObl.get_obj())

        process_list = []
        for p in range(num_process):
                proc = Sensor_merge_lineal.Sensor(listObl, p, tamano)
                process_list.append(proc)


        for x in range(num_process):
                process_list[x].start()

        alarmas(listObl,num_process)#.start()

        for x in range(num_process):
                process_list[x].join()
