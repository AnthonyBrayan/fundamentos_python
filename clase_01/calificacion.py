
"""
Crea un programa en Python que encuentre y muestre la calificación más alta de un grupo de estudiantes.

keyboard_arrow_down

Requisitos:
Se te proporciona una lista de calificaciones de estudiantes.
Debes recorrer la lista utilizando un bucle for.
Usa una variable para almacenar la calificación más alta encontrada hasta el momento.
Compara cada elemento de la lista con la calificación más alta almacenada y actualiza esta variable si encuentras una calificación mayor.
Al final, muestra la calificación más alta utilizando un mensaje en pantalla.

"""

calificaciones = [80, 60, 50, 65, 75, 55]
nota_mayor = 0

for nota in calificaciones:
    if nota > nota_mayor:
        nota_mayor = nota

print(f"La nota mayor es : {nota_mayor}")


"""
Escribe un programa que imprima los números del 1 al 100, pero aplicando las siguientes reglas:
Si el número es divisible por 3, imprime "Fizz" en lugar del número
Si el número es divisible por 5, imprime "Buzz" en lugar del número
Si el número es divisible tanto por 3 como por 5, imprime "FizzBuzz"
En cualquier otro caso, imprime el número
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 ...
"""

cont = 1

while cont > 0:
    print
