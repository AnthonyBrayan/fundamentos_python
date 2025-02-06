salario_anual= input("Ingrese el salario bruto anual: ")

salario_anual = float(salario_anual)

if salario_anual <= 10_000:
    impuesto= 5

elif salario_anual <= 20_000:
    impuesto= 10

elif salario_anual <=35_000:
    impuesto= 15

elif salario_anual <= 60_000:
    impuesto= 20

else: impuesto= 30


monto_impuesto= salario_anual*(impuesto/100)
salario_neto= salario_anual-monto_impuesto

print(f"Su salario bruto es {salario_anual}")
print(f"El porcentaje aplicado es {impuesto}%")
print(f"El monto de impuesto a pagar {monto_impuesto}")
print(f"El salario neto final: {salario_neto}")