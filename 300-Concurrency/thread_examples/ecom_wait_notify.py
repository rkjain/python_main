#!/usr/bin/env python3
from threading import *
from time import *

# Thread communication using wait, notify and notify all
# are available in class condition
# Invoke wait method on consumer obj
# Producer method invokes notfiy or notifyAll when  ready
# All threads need to work in a locked context

class Producer:

	def __init__(self):
		self.orders = []
		self.c = Condition()

	def produce(self, n):
		self.c.acquire()
		tn = current_thread().getName()
		for i in range(1, n + 1):
			print("%s => Preparing Order: Item - %s" % (tn, i))
			self.orders.append("Item - %s" % (i))
			sleep(1)
		print("%s => Orders Ready to Ship" % (tn))
		self.c.notify()
		self.c.release()

class Consumer:
	def __init__(self, prod):
		self.prod = prod

	def consume(self):
		self.prod.c.acquire()
		self.prod.c.wait(timeout=0)
		self.prod.c.release()
		tn = current_thread().getName()
		print("Shipping Items: ")
		for i in self.prod.orders:
			print(i)

prod = Producer()
con = Consumer(prod)

t1 = Thread(target=prod.produce, args=(15,))
t2 = Thread(target=con.consume)

t1.start()
t2.start()
