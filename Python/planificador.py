import threading
import random
import time

# Threading tools
lock = threading.Lock()
condition = threading.Condition()

timing = 0
unidades = 4

def sayPrompt():
	print("1.-Tiempo de Llegada\n2.-Duracion mas Corta\n3.-Prioridad mas Alta\n4.-Round-Robin")
	option = int(input("Choose one from the options: "))
	print("\nCada cuantos Scheduler quieres que se imprima: ")
	global timing
	timing  = int(input())
	return option


def randLlegada():
	return random.randrange(4)+1

def randDuracion():
	return random.randrange(50)+1

def randPrioridad():
	return random.randrange(10)+1


class Proceso():

	def __init__(self, nombre, llegada, duracion, prioridad):
		self.nombre = nombre
		self.llegada = llegada
		self.duracion = duracion
		self.prioridad = prioridad


class Scheduler(threading.Thread):

	def __init__(self, name, kind, procesos):
		threading.Thread.__init__(self)
		self.name = name
		self.kind = kind
		self.procesos = procesos
		pass

	def run(self):
		self.setup()

	def setup(self):
		if self.kind >= 1 and self.kind <= 3:
			self.priorityQueue()
		elif self.kind == 4:
			self.roundRobin()

	def priorityQueue(self):
		global unidades
		global timing
		
		while self.procesos:
			for idx, i in enumerate(self.procesos):
				while i.duracion > 0:
					i.duracion -= unidades
					if i.duracion < 0:
						i.duracion = 0
					print("{}=>{} == [{}] | [{}] | [{}]".format(self.name, i.nombre, i.llegada, i.duracion, i.prioridad))
				del self.procesos[idx]


	def roundRobin(self):
		global unidades
		global timing

		while self.procesos:
			for idx, i in enumerate(self.procesos):
				if i.duracion > 0:
					i.duracion -= unidades
					if i.duracion < 0:
						i.duracion = 0
					print("{}=>{} == [{}] | [{}] | [{}]".format(self.name, i.nombre, i.llegada, i.duracion, i.prioridad))
				else:
					del self.procesos[idx]


def main():

	kind = sayPrompt()

	procs = []

	llegada = [ randLlegada() for i in range(10)]
	duracion = [ randDuracion() for i in range(10)]
	prioridad = [ randPrioridad() for i in range(10)]

	if kind == 1:
		llegada = sorted(llegada)
	elif kind == 2:
		duracion = sorted(duracion)
	elif kind == 3:
		prioridad = sorted(prioridad, reverse=True)


	for i in range(10):
		procs.append(Proceso("P{}".format(i) , llegada[i], duracion[i], prioridad[i]))

	threads = [Scheduler("TH1",kind, procs), Scheduler("TH2", kind, procs)]


	if kind == 1:
		print("Ejecucion por Tiempo de Llegada...", end='\n')
	elif kind == 2:
		print("Ejecucion por Duracion mas Corta...", end='\n')
	elif kind == 3:
		print("Ejecucion por Prioridad Alta...", end='\n')
	elif kind == 4:
		print("Ejecucion por Round-Robin...", end='\n')

	print("Thread | Proceso [Llegada] | [Duracion] | [Prioridad]")

	for t in threads:
		t.start()
		t.join()

print("Scheduler Terminado")

if __name__ == "__main__":
	main()