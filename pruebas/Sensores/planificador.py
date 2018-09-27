import random, multiprocessing
import time
import Sensor

def alarmas(num_process, lista):

    while 1:
        for i in range (0,num_process):
            time.sleep(random.randint(0,1))
            print(lista)
            if (lista[i] < 3):
#                print(lista)
                print ("Error ", str (i))

if __name__ == '__main__':


    with multiprocessing.Manager() as manager:
        num_process = 1
        lista=manager.list(range(num_process))
        lista = [100 for i in range(num_process)] #inicializamos con 100
#        print(lista)

        sensores=[Sensor.Sensor(lista, i) for i in range(num_process)]

        alarma = multiprocessing.Process(target=alarmas, args=(num_process,lista))

        for s in sensores:
            s.start()

        alarma.start()

        for s in sensores:
            s.join()

        alarmas.join()
