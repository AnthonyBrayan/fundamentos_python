#Ejercicio de variables en Python 🐍

##Ejercicio 01: Información Personal
print("================Ejercicio 01=================")
"""

Crear variables para almacenar:
- Nombre
- Edad
- Tu altura en metros
- Si eres estudiante o no

Muestra toda la información en pantalla con un formato agradable.

"""

nombre = "Anthony Brayan"
edad = 29
altura = 1.60 
estudiante = False

print(f"Nombre: {nombre},\nEdad: {edad},\nAltura: {altura},\n¿Eres estudiante?:{estudiante}")

##Ejercicio 02: Intercambio de variables.
print("================Ejercicio 02=================")
"Crea dos variables."
a = 5
b= 10

"Intercambia las variables sin usar una tercera variable"
print(f"Valor de a: {a}\nValor de b: {b} ")

a,b = b,a

print(f"Nuevo valor de a: {a}\nNuevo valor de b: {b}")