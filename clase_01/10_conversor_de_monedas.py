# Conversor de monedas de Euros a Dólares
# Pedimos al usuario la cantidad de euros
monto_euros = input("Ingrese el monto que quieres cambiar: ")

# Convertir el texto que ingresó el usuario a decimal
euro= float(monto_euros)

# El valor de euro/dolar
valor_dolar= 0.96

# Conversión
dolares= euro/valor_dolar

# Redondear el resultado a 2 decimales
dolares = round(dolares,2)

# Mostrar el resultado
print(f"Tienes €/{str(monto_euros)} euros, en dólares es: ${str(dolares)}")