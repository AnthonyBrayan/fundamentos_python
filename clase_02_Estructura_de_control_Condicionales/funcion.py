"""
EJERCICIO: crear una función para restar números, otra para dividir y otra para multiplicar. 
** En la de dividir si se intenta dividir por cero se tiene que devolver el mensaje :
"No se puede dividir por cero"
"""
numero_1= float(input("Ingresa primer número: "))
numero_2= float(input("Ingresa segundo número: "))

def dividir(numero_1, numero_2):

    if(numero_2 == 0):
        return 'No se puede dividir entre 0'
    else:
        division= numero_1//numero_2
        return division

resultado_division = dividir(numero_1, numero_2)
print(resultado_division)