import java.util.Random

// Extending the Thread class to implement threads.
class Operaciones(val cuenta: Cuenta): Thread() {

    public override fun run() {
      // println("${Thread.currentThread()} has run.")
      synchronized(this){
        operando()
      }
    }

    public fun operando() {
      synchronized(this) {
        for ( i in 0..2 ) {
          when( getRandom(2) ) {
            1 -> {
              val mas: Int = getRandom(100)
              cuenta.ponerSaldo( mas )
              println("Se le deposito $mas a la cuenta")
            }
            2 -> {
              val menos: Int = getRandom(100)
              if ( cuenta.saldo >= menos ){
                cuenta.quitarSaldo( menos )
                println("Se le retiro $menos a la cuenta")
              } else
                println("No Hay Saldo Disponible")
            }
          }
        }
      }
    }
}

fun getRandom(max: Int) : Int = Random().nextInt(max)+1

class Cuenta(var saldo: Int) {
    
    public fun ponerSaldo(saldo: Int) { 
      synchronized(this) {
        this.saldo += saldo
      }
    }
    
    public fun quitarSaldo(saldo: Int) { 
      synchronized(this) {
        this.saldo -= saldo 
      }
    }
}

fun main(args: Array<String>) {
  val cuenta: Cuenta = Cuenta(500)

  val personas: Array<Operaciones> = arrayOf(Operaciones(cuenta), Operaciones(cuenta), Operaciones(cuenta), Operaciones(cuenta), Operaciones(cuenta))

  println("Saldo Incial ${cuenta.saldo}\n")

  for ( i in 0..4 )
    personas[i].start()

  Thread.sleep(500)
  println("\nSaldo Final ${cuenta.saldo}")
}