import random
import sys
import time
from threading import *
import queue
random.seed()

#crea una lista con valores entre 0 y 10 (enteros)
#devuelve la lista de enteros


    #calcula la suma acumulada de todos lo valores de la lista
def sumList(inList):
    finalSum = 0
    for value in inList:
        finalSum = finalSum + value
    return finalSum

class Tarea(Thread):

    def __init__(self, N, q):
        Thread.__init__(self)
        self.N = N
        self.q = q

    def genList(self, size):
        randomList = []
        for i in range(size):
            randomList.append(random.randint(0,10))
        return randomList

    #calcula la suma acumulada de todos lo valores de la lista
    def sumList(self, inList):
        finalSum = 0
        for value in inList:
            finalSum = finalSum + value
        return finalSum

    #crea una lista, suma los valores de la lista y coloca el resultado en una cola
    def run(self):
        #crea una lista de enteros aleatorios
        myList = self.genList (self.N)
        #suma los valores de la lista generadas
        finalSum = self.sumList(myList)
        # guarda el resultado en la cola (Compartida por demas procesos)
        self.q.put(finalSum)


if __name__ == '__main__':

  if len(sys.argv) == 2 and sys.argv[1].isdigit():

    N = int(sys.argv[1]) #argumento convertido en entero
    startTime = time.time() #tiempo de inicio
    q = queue.Queue() # cola para compartir resultados

    #defino cantidad de procesos que se corren
    num_process = 4

    # for i in range(0,lenProcess):
    # print (nameProcess[i])

    # defino threads

    tareas = [Tarea(N//num_process, q) for i in range(num_process)]

    for t in tareas:
        t.start()

    results = []

    # reservo lugares en el array uno por cada proceso
    for i in range(0,num_process):
        #set block=True para bloquea la asignacion hasta que el resultado este disponible en la cola
        results.append(q.get(True))

    #sum the partial results to get the final result
    finalSum = sumList(results)

    for t in tareas:
        t.join()

    endTime = time.time() #obtener el tiempo de finalizado
    workTime =  endTime - startTime #calculo del tiempo para completar el trabajo

    #imprimo resultados
    print ("Tiempo total " + str(workTime) + " segundos")
    print ("Suma del resultado final: " + str(finalSum) )

  else:
    exit(-1)
