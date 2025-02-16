#========================================================
#Variables
#========================================================

nombre = "Anthony"
edad = 29
altura = 1.70
es_estudiante = False

#Mostramos sus variables y sus tipos
print(f"Nombre: {nombre}, tipo: {type(nombre)}")
print(f"Edad: {edad}, tipo: {type(edad)}")
print(f"Altura: {altura}, tipo: {type(altura)}")
print(f"¿Es estudiante? {es_estudiante}, tipo: {type(es_estudiante)}")

#Las variables pueden cambiar su valor durante el programa
edad = 30 #Cambiar valor
print(f"Nueva edad: {edad}")

nombre = "Brayan"
print(f"Nuevo nombre:{nombre}")

#Operaciones entre variables
#Operaciones con números
precio = 100
descuento = 20

precio_final= precio - descuento
print(f"Precio final = {precio_final}")

#Operaciones con string (texto)
nombres = "Anthony Brayan"
apellidos = "Farroñan Carranza"
nombre_completo = nombres + " " + apellidos #Concatenación
print(f"Nombre completo: {nombre_completo}")

#Reglas y convenciones para nombres de variables
nombrePersona = "Anthony" #cameCase
nombre_persona = "Brayan" #snake_case (recomendado en Python)
VALOR_MAXIMO = 100 #Mayúsculas para variables constantes

#Nombres NO válidos
# 1variables = 10  # No se puede empezar con número
# mi-variable = 20 # No puede contener guiones
# class = 30       # No puede ser una palabra clave