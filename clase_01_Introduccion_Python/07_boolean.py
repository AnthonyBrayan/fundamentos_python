# Valores booleanos
# En python, en python los booleanos pueden ser True o False

verdadero = True
falso = False
print("----- Valores Booleanos -----")
print(f"Verdadero: {verdadero}")
print(f"Falso: {falso}")

# Booleanos invertidos
verdadero_invertido = not verdadero
falso_invertido= not falso
print("\n----- Booleanos invertidos -----")
print(f"Valor verdadero invertido: {verdadero_invertido}")
print(f"Valor falso invertido: {falso_invertido}")
print(f"Tipo de verdadero invertido: {type(verdadero_invertido)}")

# Doble inversión (vuelve al valor original)
verdadero_doble_invertido= not not verdadero
falso_doble_invertido= not not falso

print("\n----- Valores Booleanos con doble inversión -----")
print(f"Doble negación verdadero: {verdadero_doble_invertido}")
print(f"Doble negación falso: {falso_doble_invertido}")