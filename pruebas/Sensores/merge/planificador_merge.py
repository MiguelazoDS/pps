import Sensor_matrices
import random
import time
from multiprocessing import Process, Manager, Lock
from multiprocessing.managers import BaseManager


def alarmas(object, num_process):

    while 1:
        time.sleep(random.randint(15,16))
        lista = object.get_obj()
        print("Vigilante " , lista)
        for i in range (0,num_process):
            tiempo = time.time() - lista[i]
            print (tiempo)



class ListObj(object):
        def __init__(self, lista):
                self.lista = lista

        def set_value(self, indice_lista, codigo_alarma):
                self.lista[indice_lista] = codigo_alarma

        def get_obj(self):
                return self.lista


if __name__=="__main__":

        BaseManager.register('ListObj', ListObj)
        manager = BaseManager()
        manager.start()

        num_process = 5 #cantidad de senores
        tamano_de_matriz = 100000

        lista=list(range(num_process))
        lista = [100 for i in range(num_process)] #inicializamos con 100
        listObl = manager.ListObj(lista)

        print(listObl.get_obj())

        process_list = []
        for p in range(num_process):
                proc = Sensor_matrices.Sensor(listObl, p, tamano_de_matriz)
                process_list.append(proc)


        for x in range(num_process):
                process_list[x].start()

        alarmas(listObl,num_process).start()

        for x in range(num_process):
                process_list[x].join()
