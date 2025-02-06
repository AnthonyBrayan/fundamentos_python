
monto_euros = input("Ingrese el monto que quieres cambiar: ")

euro= float(monto_euros)

tipo_cambio= 0.96

#Convertir
dolares= euro/tipo_cambio

#Redondear
dolares = round(dolares,2)


print(f"Tienes {monto_euros} euros, en dólares es: {dolares}")