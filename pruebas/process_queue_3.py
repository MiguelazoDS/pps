import random
import sys
import time
from multiprocessing import Process, Queue
random.seed()

#crea una lista con valores entre 0 y 10 (enteros)
#devuelve la lista de enteros
def genList (size):
    randomList = []
    for i in range(size):
        randomList.append(random.randint(0,10))     
    return randomList

#calcula la suma acumulada de todos lo valores de la lista
def sumList(inList):
    finalSum = 0
    for value in inList:
        finalSum = finalSum + value
    return finalSum

#crea una lista, suma los valores de la lista y coloca el resultado en una cola
def doWork(N,q):
    #crea una lista de enteros aleatorios
    myList = genList (N)
    #suma los valores de la lista generadas
    finalSum = sumList(myList)
    # guarda el resultado en la cola (Compartida por demas procesos)
    q.put(finalSum)

if __name__ == '__main__':

  if len(sys.argv) == 2 and sys.argv[1].isdigit():

    N = int(sys.argv[1]) #argumento convertido en entero
    startTime = time.time() #tiempo de inicio
    q = Queue() # cola para compartir resultados

    #defino cantidad de procesos que se corren
    num_process = 4


    # creo nombres para procesos
    nameProcess = []
    for i in range(0,num_process): 
      nameProcess.append("p" + str(i+1)) #arranca de 1 a 4
	
    lenProcess = len(nameProcess)
     
    # for i in range(0,lenProcess): 
    # print (nameProcess[i])

    # defino procesos
    for i in range(0,lenProcess):
      nameProcess[i]= Process(target=doWork, args=(N,q))
      nameProcess[i].start()

    results = []
    # reservo lugares en el array uno por cada proceso
    for i in range(0,lenProcess):
      #set block=True para bloquea la asignacion hasta que el resultado este disponible en la cola
      results.append(q.get(True))

    #sum the partial results to get the final result
    finalSum = sumList(results)

    #join para cada proceso      
    for i in range(0,lenProcess):
      nameProcess[i].join()

    endTime = time.time() #obtener el tiempo de finalizado
    workTime =  endTime - startTime #calculo del tiempo para completar el trabajo
         
    #imprimo resultados
    print ("Tiempo total " + str(workTime) + " segundos")
    print ("Suma del resultado final: " + str(finalSum) )

  else: 
    exit(-1)

