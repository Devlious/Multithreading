import sched
import time
import datetime
from functools import wraps
from threading import Thread

## Implementa la parte asíncrona de los Threads
def async(func):
    @wraps(func)
    def async_func(*args, **kwargs):
        func_hl = Thread(target=func, args=args, kwargs=kwargs)
        func_hl.start()
        return func_hl
    return async_func


## Implementa el Schedule 
def schedule(interval):

    def decorator(func):
        ## Implementacion de la funcion de intervalos
        def periodic(scheduler, interval, action, actionargs=()):
            scheduler.enter(interval, 1, periodic,
                            (scheduler, interval, action, actionargs))
            action(*actionargs)

        ## Implementacion del funcionamiento de Schedule assigando el wrappign para la funcion de impresion
        @wraps(func)
        def wrap(*args, **kwargs):
            scheduler = sched.scheduler(time.time, time.sleep)
            periodic(scheduler, interval, func)
            scheduler.run()
        return wrap
    return decorator


# Assigna la impresion cuando pasa el Schedule esperado
@async
@schedule(1)
def periodic_event():
    print(datetime.datetime.now())


if __name__ == '__main__':
    print('start')
    periodic_event()
    print('end')