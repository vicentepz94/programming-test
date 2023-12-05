Comentarios y supuestos.

1) Fizzbuzz
  a) Para el ejercicio de fizzbuzz utilicé un ciclo for en el rango de 1 a 101 (101 debido a que la funcion 'range()' puede aceptar
     valores de inicio y parar, este último omite el número en el cual indica al ciclo for que se debe detener).
  b) Luego inicialicé una variable vacía llamada "output" la cual se encarga de almacenar la palabra 'Fizz' o 'Buzz' dependiendo de si el
     número a recorrer es múltiplo de 3 o 5.
  c) dentro de este for generamos dos ciclos if para evaluar si el iterador es  multiplo de 3 o 5 con el operador módulo '&' y almacenamos el string
     'Fizz' o 'Buzz' dentro de la variable.
  e) en la evaluación del múltiplo de 5 agregamos una concatenacion a "output" con " += "Buzz" " en caso de que el número también haya sido multiplo
     de 3 previamente, solo concatenamos "Buzz".
  f) ahora solo queda imprimir la variable output o en su defecto x (el número iterador) 
