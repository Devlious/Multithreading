import threading
import random
import time

class Account():

	def __init__(self, name, acctBalance):
		self.name = name
		self.acctBalance = acctBalance

	def get_money(self):
		pass

	def set_money(self):
		pass


class Person(threading.Thread):

	def __init__(self, name):
		threading.Thread.__init__(self)
		self.name = name

	def run(self):
		for _ in range(5):
			Person.setAction(self)

	def setAction(self):
		accounts[0]

condition = threading.Condition()

persons = ["Beto", "Alan", "Fer", "Mario", "Lolo"]

accounts = [ Account(x, random.randrange(500)+1) for x in persons]

for p in persons:
	Person(p).start()