# ======================================
# STRING (CADENAS DE TEXTO) EN PYTHON
# ======================================

# 1. Creación básica de strings
print("--- Creacion de string ---")
# Strings con comillas simples o dobles
nombre = 'Anthony'
apellido = "Farroñan"
print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")

# 2. Strings con comillas especiales
# La PEP 8 no tiene preferencia, lo importante la consistencia
mensaje_01= "Don't panic"
#Comillas simples cuando el string contiene comillas dobles
mensaje_02= 'Él dijo "Hola"'
print(f" Mensaje 01 :\n  Con apostofre: {mensaje_01}")
print(f"Mensaje 02 :\n  Con cita: {mensaje_02}")

# 3. Strings multilínea
#String multilínea (triple comilla)
mensaje_03 = '''
Este es un texto
que ocupa varias
líneas
'''
print(f" Mensaje0 3 :\n  Mensaje con varias líneas: {mensaje_03}")


#Concatenación de string
print(f"Concatenación de string : ")
#Unir string con +
nombre_completo = nombre + " " + apellido
print(f"Nombre completo: {nombre_completo}")

# 4. Operaciones con strings
print("\n--- Operaciones con strings ---")
print("\n4.1 Concatenación")
nombre_completo = nombre + " " + apellido
print(f"Nombre completo: {nombre_completo}")

print("\n4.2 Multiplicación")
separador = "-" * 20
print(f"Separador: {separador}")

# 5. Acceso a caracteres
#Acceso a caracteres
print(f"Acceso a caracteres ")
texto = "Python"
print(f"Texto: {texto}")
print(f"Primer caracter: {texto[0]}")
print(f"Segundo caracter: {texto[1]}")
print(f"Último caracter: {texto[-1]}")

# 6. Formato de strings
nombre= "Jian Pierre"
edad = 26
altura = 1.70

#Usando formato format() (Es antiguo)
print("Me llamo {}, tengo {} años, y mido {} cm".format(nombre, edad, altura))


#Usando formato f-strings (Recomendado)
print(f"Me llamo {nombre}, tengo {edad} años y mido {altura} cm.")

# 7. Caracteres especiales
#Acceso a caracteres
print(f" Acceso a caracteres ")
# \n Nueva línea (salto de línea)
# \t Tabulación
# \' Comilla simple
# \" Comilla doble
# \\ Barra invertida

print("Línea 1\nLínea2")

print("Nombre:\tAna")

print("Él dijo: \"Hola\"")
