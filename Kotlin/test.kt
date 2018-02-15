import java.util.ArrayList


fun main(args: Array<String>) {
  var arr: ArrayList<Int> = ArrayList(1)
  
  for ( i in 1..5 ) {
    arr.add(i)
  }

  arr.remove(arr[arr.size-1])

  println("Length: ${arr.size} = $arr")

}