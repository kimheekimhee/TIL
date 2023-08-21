fun main(args: Array<String>) {
    println("Hello World!")

    // Try adding program arguments via Run/Debug configuration.
    // Learn more about running applications: https://www.jetbrains.com/help/idea/running-applications.html.
    println("Program arguments: ${args.joinToString()}")



    /*
    여러줄 주석
    /* 주석안에 내포된 주석 */
    */
    println("Hello") // 한줄짜리 주석

    val a = readLine()!!.toInt() // input_1
    val b = readLine()!!.toInt() // input_2
    println(a + b)

    val n: Int = 100
    val str: String = "Hello!"

    println(n)
    println(str)

    // val n: Int = "Hello!" // Error

}