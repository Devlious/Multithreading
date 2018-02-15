private val lock = java.lang.Object()

fun produce() = synchronized(lock) {  
  while (items >= maxItems) {
    lock.wait()
  }
  Thread.sleep(rand.nextInt(100).toLong())
  items++
  println("Produced, count is $items: ${Thread.currentThread()}")
  lock.notifyAll()
}

fun consume() = synchronized(lock) {  
  while (items <= 0) {
    lock.wait()
  }
  Thread.sleep(rand.nextInt(100).toLong())
  items--
  println("Consumed, count is $items: ${Thread.currentThread()}")
  lock.notifyAll()
}