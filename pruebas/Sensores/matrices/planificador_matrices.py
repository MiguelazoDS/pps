import Sensor_matrices
import random
import time
import numpy
import sys
from multiprocessing import Process, Manager, Lock
from multiprocessing.managers import BaseManager


def alarmas(object, num_process, tiempo_limite):

    #bucle de 100 para el promedio
    tiempo_inicio = time.time()


    while (1):
#        time.sleep(random.randint(1))
        lista = object.get_obj()
#        print("Vigilante " , lista)
        for i in range (0,num_process):
            if(lista[i] > 0):
                tiempo = time.time() - lista[i]
                object.set_value(i, -1)
                object.set_value_tiempos(tiempo)


#    print (tiempos_atencion )
#    media = numpy.mean(tiempos_atencion)
#    print (tiempos_atencion )
#    print (media )
#    object.set_value_promedio(media)
#    print ("termine" )


class ListObj(object):
        def __init__(self, lista, lista_tiempos_promedios):
                self.lista = lista
                self.lista_tiempos_promedios = lista_tiempos_promedios

        def set_value(self, indice_lista, tiempo_atencion):
                self.lista[indice_lista] = tiempo_atencion

        def set_value_tiempos(self, tiempo_atencion):  #para estadistica
                self.lista_tiempos_promedios.append(tiempo_atencion)

        def get_obj(self):
                return self.lista

        def get_value_tiempos(self): #para estadistica
                return self.lista_tiempos_promedios


if __name__=="__main__":
        num_process = 1
        tamano_de_matriz = 10
        if len(sys.argv) >2:
            temp1=int(sys.argv[2])
            if sys.argv[2].isdigit() and temp1 > 10 and temp1 < 100000:
                tamano_de_matriz=temp1#cantidad de valores
        if len(sys.argv) >1:
            temp2=int(sys.argv[1])
            if sys.argv[1].isdigit() and temp2 > 1 and temp2 < 100:
                num_process = temp2 #cantidad de sensores

        BaseManager.register('ListObj', ListObj)
        manager = BaseManager()
        manager.start()

        tiempo_limite = 5 #tiempo que corre alarmas

#        while(num_process < 3 ):

#            num_bucles = num_bucles-1

        lista=list(range(num_process))
        lista = [-1 for i in range(num_process)] #inicializamos con -1
        lista_tiempos_promedios = []
        listObl = manager.ListObj(lista,lista_tiempos_promedios)

        #print(listObl.get_obj())

        process_list = []
        for p in range(num_process):
                proc = Sensor_matrices.Sensor(listObl, p, tamano_de_matriz)
                process_list.append(proc)


        for x in range(num_process):
                process_list[x].start()

        alarmas= Process(target=alarmas, args=(listObl,num_process, tiempo_limite))
        alarmas.start()

        time.sleep(tiempo_limite)

        for x in range(num_process):
                process_list[x].terminate()

        alarmas.terminate()

#            print (listObl.get_value_tiempos() )
        media = numpy.mean(listObl.get_value_tiempos() ) #promedio de ti
        print(media)

    #        for x in range(num_process):
    #                process_list[x].join()
