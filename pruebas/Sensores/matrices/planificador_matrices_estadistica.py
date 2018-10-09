import Sensor_matrices
import random
import time
import numpy
from multiprocessing import Process, Manager, Lock
from multiprocessing.managers import BaseManager


def alarmas(object, num_process,tiempo_limite):

    #bucle de 100 para el promedio
    tiempo_inicio = time.time()

    tiempos_atencion = [] #arreglo con tiempos


    while ((time.time() - tiempo_inicio) < tiempo_limite):
#        time.sleep(random.randint(1))
        lista = object.get_obj()
#        print("Vigilante " , lista)
        for i in range (0,num_process):
            if(lista[i] > 0):
                tiempo = time.time() - lista[i]
                tiempos_atencion.append(tiempo)
                object.set_value(i, -1)
                #print (tiempos_atencion )

#    print (tiempos_atencion )
    print (numpy.mean(tiempos_atencion) )
    print ("termine" )


class ListObj(object):
        def __init__(self, lista, valor_promedio):
                self.lista = lista
                self.valor_promedio = valor_promedio

        def set_value(self, indice_lista, tiempo_atencion):
                self.lista[indice_lista] = tiempo_atencion

        def set_value_promedio(self, tiempo_atencion_promedio):  #para estadistica
                self.valor_promedio = tiempo_atencion_promedio

        def get_obj(self):
                return self.lista

        def get_value_promedio(self): #para estadistica
                return self.valor_promedio


if __name__=="__main__":

        BaseManager.register('ListObj', ListObj)
        manager = BaseManager()
        manager.start()

        num_process = 3 #cantidad de senores
        tamano_de_matriz = 1000000
        tiempo_limite = 3 #tiempo que corre alarmas antes de detener la ejecucion
        num_bucles = 1

        while((num_bucles = num_bucles-1 ) < 0 )

            lista=list(range(num_process)) #lista donde cada proceso pone sus valores
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

            alarmas.join()

            for x in range(num_process):
                    process_list[x].join()
