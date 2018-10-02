from multiprocessing import Process, Manager, Lock
from multiprocessing.managers import BaseManager
import numpy as np

class NestedObj(object):
       def __init__(self):
                self.val = 1

class CustomObj(object):
        def __init__(self, numpy_obj):
                self.numpy_obj = numpy_obj
                self.nested_obj = NestedObj()

        def set_value(self, p, q, v):
                self.numpy_obj[p, q] = v

        def get_obj(self):
                return self.numpy_obj

        def get_nested_obj(self):
                return self.nested_obj.val

class CustomProcess(Process):
        def __init__(self, obj, p, q, v):
                super(CustomProcess, self).__init__()
                self.obj = obj
                self.index = p, q
                self.v = v

        def run(self):
                self.obj.set_value(*self.index, self.v)



if __name__=="__main__":
        BaseManager.register('CustomObj', CustomObj)
        manager = BaseManager()
        manager.start()
        data = [[0 for x in range(10)] for y in range(10)]
        matrix = np.matrix(data)
        custom_obj = manager.CustomObj(matrix)
        print(custom_obj.get_obj())
        process_list = []
        for p in range(10):
                for q in range(10):
                        proc = CustomProcess(custom_obj, p, q, 10*p+q)
                        process_list.append(proc)
        for x in range(100):
                process_list[x].start()
        for x in range(100):
                process_list[x].join()
        print(custom_obj.get_obj())
        print(custom_obj.get_nested_obj())




import Sensor
import random
import time
from multiprocessing import Process, Manager, Lock
from multiprocessing.managers import BaseManager


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

        num_process = 2

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
        for x in range(num_process):
                process_list[x].join()

#        print(custom_obj.get_obj())
