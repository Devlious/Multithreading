import java.util.Random
//import kotlin.concurrent.thread

data class Cuenta(var saldo: Int)

fun getRandom(max: Int) : Int = Random().nextInt(max)+1

class Operaciones(private val cuenta: Cuenta) : Thread() {

  @Volatile private var saldo = 2
  private val rand = Random()

  private val lock = java.lang.Object()

  override fun run() {
    for ( i in 0..14 ) {
      when( getRandom(2) ) {
        1 -> produce()
        2 -> consume()
      }
    }
  }

  fun produce() = synchronized(lock) {
    while (saldo >= cuenta.saldo) {
      println("Waiting Produce ${Thread.currentThread()}")
      lock.wait()
    }
    Thread.sleep(200)
    //if ( saldo+2 < cuenta.saldo)  
      saldo += 2
    //else
    //  saldo += 1
    
    println("Produced, count is $saldo")
    lock.notifyAll()
  }

  fun consume() = synchronized(lock) {
    while (saldo <= 0) {
      println("Waiting Consume ${Thread.currentThread()} --- Saldo = ${saldo}")
      lock.wait()
    }
    Thread.sleep(200)
    saldo--
    println("Consumed, count is $saldo")
    //lock.notifyAll()
  }
}

fun main(args: Array<String>) {
  println("Starting...")

  val cuenta: Cuenta = Cuenta(5)

  val operaciones: Array<Operaciones> = arrayOf( Operaciones(cuenta), 
                                                 Operaciones(cuenta), 
                                                 Operaciones(cuenta))

  for (j in 0..2) {
    operaciones[j].start()
  }

  //Thread.sleep(1000)
  //println("...finishing")
}

<link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.blue-light_green.min.css" />