#https://gist.github.com/cristipufu/2d8724a7b526ef57e73a4f1709fa5690
#https://stackoverflow.com/questions/12474182/asynchronously-read-and-process-an-image-in-python
import sys
import random
import time
import multiprocessing
import scipy.misc
from multiprocessing import Semaphore, Queue

import cv2
import numpy as np
from matplotlib import pyplot as plt

class Producer(multiprocessing.Process):

	lista = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg","6.jpg","7.jpg",
			 "8.jpg","9.jpg", "10.jpg", "11.jpg" , "12.jpg"]

	def __init__(self, images, can_produce, can_consume):
		multiprocessing.Process.__init__(self)
		self.images = images
		self.can_produce = can_produce
		self.can_consume = can_consume

	def produce_images(self):
		for f in self.lista:
		#	self.wait()
			images.put(scipy.misc.imread(f))
			self.can_consume.release() #aumento en uno la cantidad de permisos
			print ("{}: i produced an images".format(self.name))
		#	images.put(scipy.misc.imread('python.jpg'))


	def wait(self):
		time.sleep(random.uniform(0, 3))

	def run(self):
		#Espera un tiempo, hace el aqcuire si hay lugar en la cola de semaforos
		#para producir (cantidad de permisos menor a la del tamano del buffer),
		#en caso de que no pueda hacer el acquire se queda esperando el release
		#del consumidor. Cuando produce un item hace un release en el semaforo
		#del consumidor (aumenta en una unidad los permisos).
#		while 1:
		#	self.wait()
		self.can_produce.acquire() #disminuye en uno la cantidad de permisos
		self.produce_images()
#		self.can_consume.release() #aumento en uno la cantidad de permisos

class Consumer(multiprocessing.Process):

	def __init__( self, images, can_produce, can_consume ):
		multiprocessing.Process.__init__(self)
		self.images = images
		self.can_produce = can_produce
		self.can_consume = can_consume

	def consume_images(self):
		try:
			img = images.get()
			edges = cv2.Canny(img,100,200)
			name = "./procesadas/" + str(random.randint(1, 1000))  +".jpg"
			cv2.imwrite(name,edges)
			#cv2.imwrite(name,img)
			print ("{}: i consumed an images".format(self.name))
		except Queue.Empty:  # Queue here refers to the  module, not a class
			print ('foo')


	def wait(self):
		time.sleep(random.uniform(0, 3))

	def run(self):
		#Hace el aqcuire si hay lugar en la cola de semaforos
		#para consumir en caso de que no pueda hacer el acquire se queda
		#esperando el release del productor. Cuando consume un item hace un
		#release en el semaforo del prodcutor (aumenta en una unidad los permisos).
		while 1:
#			self.wait()
			self.can_consume.acquire()  #disminuye en uno la cantidad de permisos
			self.consume_images()
			self.can_produce.release()  #aumento en uno la cantidad de permisos


if __name__ == "__main__":

	#ingreso por linea de comando cantidad de productores, consumidores y tamano de buffer
	if len(sys.argv) != 4:
		usage(sys.argv[0])
		sys.exit(0)

	#count_producers = int(sys.argv[1])
	count_producers = 1
	count_consumers = int(sys.argv[2])
	buffer_length = 15

	images = Queue()
	producers = []
	consumers = []

	#acquire mientras buffer no esta full
	#crea semaforo con una cantidad "buffer_length" de permisos
	can_produce = Semaphore(buffer_length)

	#acquire mientras buffer no este vacio
	#crea semaforo con 0 de permisos que va llenando a medida que se produce
	can_consume = Semaphore(0)

	producers = [Producer(images, can_produce, can_consume) for i in range(count_producers)]
	consumers = [Consumer(images, can_produce, can_consume) for i in range(count_consumers)]

	for p in producers:
		p.start()

	for c in consumers:
		c.start()

	for p in producers:
		p.join()

	for c in consumers:
		c.join()
