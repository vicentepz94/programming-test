Comentarios y supuestos.

1. Fizzbuzz
   a) Para el ejercicio de fizzbuzz utilicé un ciclo for en el rango de 1 a 101 (101 debido a que la funcion 'range()' puede aceptar
   valores de inicio(opcional) y parar, este último omite el número en el cual indica al ciclo for que se debe detener).
   b) Luego inicialicé una variable vacía llamada "output" la cual se encarga de almacenar la palabra 'Fizz' o 'Buzz' dependiendo de si el
   número a recorrer es múltiplo de 3 o 5.
   c) dentro de este for generamos dos ciclos if para evaluar si el iterador es multiplo de 3 o 5 con el operador módulo '&' y almacenamos el string
   'Fizz' o 'Buzz' dentro de la variable.
   e) en la evaluación del múltiplo de 5 agregamos una concatenacion a "output" con " += "Buzz" " en caso de que el número también haya sido multiplo
   de 3 previamente, solo concatenamos "Buzz".
   f) ahora solo queda imprimir la variable output o en su defecto x (el número iterador)

2. ORM
   Para este ejercicio intenté representar el funcionamiento de un ORM con conocimiento de clases y funciones para obtener un resultado similar.
   utilicé el metodo **str** para devolver un string del contenido de la clase Book.
   a) utilicé la clase SQL como clase padre de Book para realizar las funciones dentro de esta, luego construí la clase solicitando los argumentos: 'title', 'author', y 'description', declarando los mismos elemntos y agregando un id vacio.
   c) Para la función de crear libro 'save' utilicé la variable de la clase SQL ya implementada en el ejercicio para generar la id y luego use la función de create de la clase SQL.
   d) Para la función delete se llamó a la función de la clase SQL delete y luego se utilizó la keyword del para eliminar el objeto.
   e) Las funciones list y retrieve no supe implementarlas.

3. Indexing de multiniveles
   a) para este ejercicio, dentro de la funcion 'multilevel_index', inicié la variable de tipo diccionario'index = {}' con el fin de almacenar los datos e inicialicé la variable iLevel para almacenar el nivel de index.
   b) generé un ciclo principal for para iterar por cada diccionario de la lista 'documents'.
   c) luego iteré las 'keys' por cada 'document' almacenando el valor de 'key' en la variable 'value'.
   d) luego utilice el condicional if para evaluar si la variable 'value' no se encuentra en 'iLevel', de no encontrarla la asigno como primer nivel del diccinario a iLevel.
   e) para evaluar el segundo elemento dentro de la lista del argumento 'keys' y asi agregarla como segundo nivel del diccionario, utilicé un if con el valor de indice de lista 'keys[-1]' para verificarr si ya existia dentro del iLevel, de no ser asi asignarla como valor clave con un valor de lista vacio.
   f) luego a este valor le agregué el contenido de document con el metodo de lista 'append' y finalmente imprimí la variable index.
