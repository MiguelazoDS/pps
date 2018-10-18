#https://gist.github.com/cristipufu/2d8724a7b526ef57e73a4f1709fa5690
#La clase threading utiliza todos lo cores
#Funciona en 2.7 y 3.7
#En 2.7 no se puede cancelar el proceso desde la termina con ctrl+c
import sys
import random
import time
from threading import *

class Producer(Thread):
	def __init__(self, items, can_produce, can_consume):
		Thread.__init__(self)
		self.items = items
		self.can_produce = can_produce
		self.can_consume = can_consume

	def produce_item(self):
		self.items.append(1)
		print ("{}: i produced an item".format(self.name))

	def wait(self):
		time.sleep(random.uniform(0, 3))

	def run(self):
		#Espera un tiempo, hace el aqcuire si hay lugar en la cola de semaforos
		#para producir (cantidad de permisos menor a la del tamano del buffer),
		#en caso de que no pueda hacer el acquire se queda esperando el release
		#del consumidor. Cuando produce un item hace un release en el semaforo
		#del consumidor (aumenta en una unidad los permisos).
		while 1:
			self.wait()
			self.can_produce.acquire() #disminuye en uno la cantidad de permisos
			self.produce_item()
			self.can_consume.release() #aumento en uno la cantidad de permisos

class Consumer(Thread):
	def __init__(self, items, can_produce, can_consume):
		Thread.__init__(self)
		self.items = items
		self.can_produce = can_produce
		self.can_consume = can_consume

	def consume_item(self):
		item = self.items.pop() #remueve y devuelve el ultimo objeto de la lista
		print ("{}: i consumed an item".format(self.name))

	def wait(self):
		time.sleep(random.uniform(0, 3))

	def run(self):
		#Espera un tiempo, hace el aqcuire si hay lugar en la cola de semaforos
		#para consumir en caso de que no pueda hacer el acquire se queda
		#esperando el release del productor. Cuando consume un item hace un
		#release en el semaforo del prodcutor (aumenta en una unidad los permisos).
		while 1:
			self.wait()
			self.can_consume.acquire()  #disminuye en uno la cantidad de permisos
			self.consume_item()
			self.can_produce.release()  #aumento en uno la cantidad de permisos

def usage(script):
	print ("Usage:\t%s count_producers count_consumers buffer_length" % script)

if __name__ == "__main__":

	#ingreso por linea de comando cantidad de productores, consumidores y tamano de buffer
	if len(sys.argv) != 4:
		usage(sys.argv[0])
		sys.exit(0)

	count_producers = int(sys.argv[1])
	count_consumers = int(sys.argv[2])
	buffer_length = int(sys.argv[3])

	items = []
	producers = []
	consumers = []

	#acquire mientras buffer no esta full
	#crea semaforo con una cantidad "buffer_length" de permisos
	can_produce = Semaphore(buffer_length)

	#acquire mientras buffer no este vacio
	#crea semaforo con 0 de permisos que va llenando a medida que se produce
	can_consume = Semaphore(0)

	for i in range(count_producers):
		producers.append(Producer(items, can_produce, can_consume))
		producers[-1].start()

	for i in range(count_consumers):
		consumers.append(Consumer(items, can_produce, can_consume))
		consumers[-1].start()

	for p in producers:
		p.join()

	for c in consumers:
		c.join()
