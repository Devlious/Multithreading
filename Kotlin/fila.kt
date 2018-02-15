import java.util.ArrayList
import java.util.Random

class Cuenta(var arr: ArrayList<Int>?) : Thread() {

  @Synchronized
  public override fun run() {

    for ( i in 1..3 ) {
      when( getRandom(2) ) {
        1 -> addNum()
        2 -> removeNum()
      }
    }

  }

  @Synchronized
  public fun addNum() {
      if ( arr!!.size < 3 ) {
        arr!!.add( getRandom(10) )
        println("${arr!![arr!!.size-1]} ha sido agregado")
      } else {
        println("El arreglo esta lleno :(")
      }
  }

  @Synchronized
  public fun removeNum() {
      if ( arr!!.size > 0 ) {
        println("[${arr!![0]}] Ha sido removido ")

        for( i in 0..arr!!.size-2 ) {
          arr!![i] = arr!![i+1]
        }
        arr!!.remove(arr!![arr!!.size-1])

      } else {
        println("No hay numeros para quitar")
      }
  }

}


fun getRandom(max: Int) : Int = Random().nextInt(max)+1

fun main(args: Array<String>) {
  var arr = ArrayList<Int>()

  var cuentas = mutableListOf<Cuenta>()

  for( i in 0..4) {
    cuentas.add(Cuenta(arr))
    cuentas[i].start()
  }

  Thread.sleep(500)

  println("Arreglo Final $arr")
}