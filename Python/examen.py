import threading
import time
import random

cntP = 0
cntC = 0
cntU = 0

namP = 0
namC = 0

personas = [ random.randrange(3)+1 for _ in range(20)]

# 1 = Preferente
# 2 = Cuenta
# 3 = Usuario

lenP = len(list(filter(lambda a: a == 1, personas)))
lenC = len(list(filter(lambda a: a == 2, personas)))
lenU = len(list(filter(lambda a: a == 3, personas)))

class Caja(threading.Thread):

	def __init__(self, name):
		threading.Thread.__init__(self)
		self.cntP = 0
		self.cntC = 0
		self.name = name

	def run(self):

		while lenP+lenC+lenU:
			condition.acquire()
			toWait = random.randrange(5)+1
			print("~[{}] has a client for <{} seconds>".format(self.name, toWait))
			Caja.asignUser(self)
			condition.wait(timeout=toWait)
			condition.release()

	def asignUser(self):
		# Counters
		global cntP
		global cntC
		global cntU
		# Lenghts
		global lenP
		global lenC
		global lenU
		# Names
		global namP
		global namC


		if (cntC == 2 or lenC <= 0) and lenU > 0:
			print(" ->Atendiendo : [U{}]\n".format(cntU+1))
			cntU += 1
			lenU -= 1
			if cntC == 2:
				cntC = 0

		elif (cntP == 2 or lenP <= 0) and lenC > 0:
			print(" ->Atendiendo : [C{}]\n".format(namC+1))
			namC += 1
			cntC += 1
			lenC -= 1
			if cntP == 2:
				cntP = 0

		elif lenP > 0:
			print(" ->Atendiendo : [P{}]\n".format(namP+1))
			namP += 1
			cntP += 1
			lenP -= 1

condition = threading.Condition()

for i in range(3):
	Caja("Caja {}".format(i+1)).start()
