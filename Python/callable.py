class Foo(object):
	## Dice que puede llamar a la clase
    def __call__(self):
        print("something")

class Bar(object):
	## inicializa la llamada a la classe Foo
    def __init__(self):
        self.foo = Foo()

    ## Instancia el objeto indicador de la clase Foo 
    def __call__(self):
        self.foo()

## inicializa b a la clase bar
b = Bar()
## Se instancia y da como resultado la llamada a la clase Foo
b()