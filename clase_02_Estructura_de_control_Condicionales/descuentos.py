"""
Ejercicio 1: Calculadora de Descuentos
Enunciado
Crear un programa que calcule el precio final de un producto con descuento. Debes crear funciones para:

Validar que el descuento esté entre 0 y 100
Calcular el precio con el descuento aplicado
Mostrar el ahorro total

Ejemplo de Ejecución=== CALCULADORA DE DESCUENTOS ===
Ingrese el precio del producto: 100
Ingrese el porcentaje de descuento: 20

-- Resumen de la compra --
Precio original: $100.00
Descuento: 20%
Ahorro: $20.00
Precio final: $80.00

=== CALCULADORA DE DESCUENTOS ===
Ingrese el precio del producto: 50
Ingrese el porcentaje de descuento: 150
Error: El descuento debe estar entre 0 y 100

"""

monto = int (input("Ingrese monto a pagar: "))

descuento = int(input("Ingresa el porcentaje de descuento: "))

def validar_descuento(descuento):
    if(descuento > 0 and descuento < 100):
        print("Descuento aceptado.")
        return True
    else:
        print("El descuento debe estar entre mayor a 0 y menor a 100")

def calcular_precio_descuento(monto, descuento):
    monto_total= monto * (descuento/100)
    return monto_total

def mostrar_ahorro(monto, descuento):
    ahorro= monto - (monto*(descuento/100))
    return ahorro


