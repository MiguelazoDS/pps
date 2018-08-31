#https://stackoverflow.com/questions/15859374/python-producer-consumer-with-process-and-pool
from multiprocessing import Manager, Process, Pool,Queue
from Queue import Empty
import time

def writer(queue):
   for i in range(1000):
     queue.put(i)
     print 'put %i size now %i'%(i, queue.qsize())
     time.sleep(2)

def reader(id, queue):
   for i in range(1000):
     try:
       cnt = queue.get(1,1)
       print '%i got %i size now %i'%(id, cnt, queue.qsize())
     except Empty:
       pass #no hace nada si la cola esta vacia
     time.sleep(6)

class Managerss:
   def __init__(self):
     self.queue= Queue()
     self.NUMBER_OF_PROCESSES = 100 #cantidad de consumidores


   def start(self): 
     #define un unico proceso productor 
     self.p = Process(target=writer, args=(self.queue,))
     self.p.start()
     #array de consumidores cada uno
     self.readers = [Process(target=reader, args=(i, self.queue,)) for i in xrange(self.NUMBER_OF_PROCESSES)]  
                        
     for w in self.readers:
       w.start()

   def join(self):
     self.p.join()
     for w in self.readers:
       w.join()

if __name__ == '__main__':
    m= Managerss()
    m.start()
    m.join()
