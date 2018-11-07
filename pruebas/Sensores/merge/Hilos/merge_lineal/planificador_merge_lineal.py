import Sensor_merge_lineal
import random
import time
import numpy
import sys
import threading

def alarmas(lista, lista_tiempos_promedios, num_process):
    tiempo_inicio = time.time()
    while (time.time()-tiempo_inicio < 5):
        for i in range (0,num_process):
            if(lista[i] > 0):
                tiempo = time.time() - lista[i]
                lista[i]= -1
                lista_tiempos_promedios.append(tiempo)

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


        tiempo_limite = 5 #tiempo que corre alarmas
        lista=list(range(num_process))
        lista = [-1 for i in range(num_process)] #inicializamos con -1
        lista_tiempos_promedios = []

        process_list = []
        for p in range(num_process):
                proc = Sensor_merge_lineal.Sensor(lista, p, tamano_de_matriz)
                process_list.append(proc)

        for x in range(num_process):
                process_list[x].start()



        alarmas= threading.Thread(target=alarmas, args=(lista, lista_tiempos_promedios, num_process))
        alarmas.start()
        #alarmas.join()

        time.sleep(tiempo_limite)

        #for x in range(num_process):
        #        process_list[x].terminate()

        #alarmas.terminate()

        media = numpy.mean(lista_tiempos_promedios) #promedio de ti
        print(media)

        for x in range(num_process):
            process_list[x].join()

        alarmas.join()
