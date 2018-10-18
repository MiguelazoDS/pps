import Sensor
import random
import time
from multiprocessing import Process, Manager, Lock
from multiprocessing.managers import BaseManager


def alarmas(object, num_process):

    while 1:
        time.sleep(random.randint(14,15))
        lista = object.get_obj()
        print("Vigilante " , lista)
        for i in range (0,num_process):
            if (lista[i] < 3):
                print ("Emergencia en ", str (i))



class ListObj(object):
        def __init__(self, lista):
                self.lista = lista

        def set_value(self, indice_lista, codigo_al            num_bucles = num_bucles-1

            lista=list(range(num_process))
            lista = [-1 for i in range(num_process)] #inicializamos con -1
            listObl = manager.ListObj(lista)

            print(listObl.get_obj())

            process_list = []
            for p in range(num_process):
                    proc = Sensor_matrices.Sensor(listObl, p, tamano_de_matriz)
                    process_list.append(proc)


            for x in range(num_process):
                    process_list[x].start()

            alarmas= Process(target=alarmas, args=(listObl,num_process, tiempo_limite))
            alarmas.start()

            for x in range(num_process):
                    process_list[x].join()

            alarmas.join()arma):
                self.lista[indice_lista] = codigo_alarma

        def get_obj(self):
                return self.lista


if __name__=="__main__":

        BaseManager.register('ListObj', ListObj)
        manager = BaseManager()
        manager.start()

        num_process = 15 #cantidad de senores

        lista=list(range(num_process))
        lista = [100 for i in range(num_process)] #inicializamos con 100
        listObl = manager.ListObj(lista)

        print(listObl.get_obj())

        process_list = []
        for p in range(num_process):
                proc = Sensor.Sensor(listObl, p)
                process_list.append(proc)


        for x in range(num_process):
                process_list[x].start()

        alarmas(listObl,num_process).start()

        for x in range(num_process):
                process_list[x].join()
