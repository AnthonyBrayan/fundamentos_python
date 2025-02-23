import random
"""
Ejercicio1: Calculadora de Impuestos 💰
Enunciado: Crea un programa que calcule el impuesto a pagar según el salario anual introducido. 
Los rangos de impuestos son:

 - Hasta $10,000: 5% de impuesto
 - De $10,001 a $20,000: 10% de impuesto
 - De $20,001 a $35,000: 15% de impuesto
 - De $35,001 a $60,000: 20% de impuesto
 - Más de $60,000: 30% de impuesto

 El programa debe mostrar:

 - El salario bruto.
 - El porcentaje de impuesto aplicado.
 - El monto de impuesto a pagar.
 - El salario neto final.
"""
# Solución: Calculadora de Impuesto.

# Pedimos el salario anual.
salario_anual = float(input("Ingrese el salario bruto anual: "))

# Inicializamos el porcentaje de impuesto.
imnpuesto = 0

# Determinamos el porcentaje según el rango.
if salario_anual <= 10_000:
    impuesto = 5
elif salario_anual <= 20_000:
    impuesto = 10
elif salario_anual <=35_000:
    impuesto = 15
elif salario_anual <= 60_000:
    impuesto = 20
else: 
    impuesto = 30

# Calculamos el impuesto y el salario neto.
monto_impuesto= salario_anual*(impuesto / 100)
salario_neto= salario_anual - monto_impuesto

# Mostramos los resultados.
print("\n=== Resumen de impuestos ===")
print(f"Su salario bruto es {salario_anual}")
print(f"El porcentaje aplicado es {impuesto}%")
print(f"El monto de impuesto a pagar {monto_impuesto}")
print(f"El salario neto final: {salario_neto}")

"""
Ejercicio 2: Piedra, Papel o Tijera ✌️
Enunciado: Crea un juego de Piedra, Papel o Tijera donde el usuario juegue contra la computadora.

 - La computadora debe elegir aleatoriamente.
 - El programa debe mostrar quién ganó y por qué.
 - Debe validar que el usuario ingrese una opción válida.
"""
# Solución
#Mostramos las opciones al usuario.
print("Juguemos a Piedra, Papel o Tijera")
print("1.- Piedra")
print("2.- Papel")
print("3.- Tijera")

# Obtenemos la eleción del usuario.
eleccion_usuario = int(input("\nElije tu opción(1-3): "))

# Validamos la entrada del usuario.
if eleccion_usuario == 1 or eleccion_usuario == 2 or eleccion_usuario == 3:
    # Generamos la elección de la computadora (1, 2, 3).
    eleccion_computadora = random.randint(1,3)

    # Mostramos la elección del usuario.
    if eleccion_usuario == 1:
        print("\nTú elegiste: Piedra")
    elif eleccion_usuario == 2:
        print("\nTú elegiste: Papel")
    else:
        print("\nTú elegiste: Tijera")

    # Mostramos la elección de la computadora.
    if eleccion_computadora == 1:
        print("\nLa computadora elegió: Piedra")
    elif eleccion_computadora == 2:
        print("\nLa computadora elegió: Papel")
    else:
        print("\nLa computadora elegió: Tijera")
    
    # Determinamos el ganador
    if eleccion_usuario == eleccion_computadora:
     print("\n¡Empate!")
    elif eleccion_usuario == 1 and eleccion_computadora == 3:
        print("\n¡Ganaste! Piedra vence a Tijera")
    elif eleccion_usuario == 2 and eleccion_computadora == 1:
        print("\n¡Ganaste! Papel vence a Piedra")
    elif eleccion_usuario == 3 and eleccion_computadora == 2:
        print("\n¡Ganaste! Tijera vence a Papel")
    else:
        print("\n¡La computadora gana!")
else:
    print("¡Opción no válida! Debes elegir 1,2,3")