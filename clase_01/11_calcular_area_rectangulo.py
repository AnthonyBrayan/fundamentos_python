"""
RETO: Calculadora de Área de Rectángulo 🟥
¡Vamos a crear una calculadora que nos ayude a encontrar el área de un rectángulo!

Tu programa debe:
1. Pedir al usuario la base del rectángulo
2. Pedir al usuario la altura del rectángulo
3. Calcular el área multiplicando base por altura
4. Mostrar el resultado en pantalla

Ejemplo de ejecución:
¿Cuál es la base del rectángulo? 5
¿Cuál es la altura del rectángulo? 3
El área del rectángulo es: 15

"""
# Pedimos la base del rectángulo.
base_rectangulo = input("Ingresa la base del rectangulo: ")
base_rectangulo = float(base_rectangulo)

# Pedimos la altura del rectángulo.
altura_rectangulo = input("Ingresa la altura del rectangulo: ")
altura_rectangulo = float(altura_rectangulo)

# Calculamos el área.
area_rectangulo = base_rectangulo * altura_rectangulo

# Mostramos el resultado.
print(f"El área del rectangulo es: {str(area_rectangulo)}")