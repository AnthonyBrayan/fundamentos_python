def numero():
    try:
        numero = int(input("Escribe un número: "))
        print(f"El número es : {numero}")
    except ValueError:
        print('Debes escribir un número válido')

numero()