from concurrent.futures import ThreadPoolExecutor
from time import sleep
 
## Funcion que hace la espera de 5 segundos y luego regresa el mensaje
def return_after_5_secs(message):
    sleep(5)
    return message
 
# Inicializa la variable pool con una ThreadPoolExecutor de 3 Threads
pool = ThreadPoolExecutor(3)

# Inicializa future con una iniciacion de ThreadPool 
future = pool.submit(return_after_5_secs, ("hello"))

# Obtenemos si Future se ha resuelto
print("FutureAsk: ", future.done())

#Esperamos 5 segundos
sleep(5)

# Obtenemos si Future se ha resuelto
print("FutureAskAfter: ", future.done())

# Obtenemos el resultado de Future
print("FutureResult: ", future.result())