
nombre = input("Nombre del trabajador: ")
horas = float(input("Horas trabajadas: "))
tarifa = float(input("Tarifa por hora: "))

if horas <= 35:
    salario_bruto = horas * tarifa
else:
    salario_bruto = 35 * tarifa + (horas - 35) * tarifa * 1.5

impuesto = 0

if salario_bruto > 500:
    impuesto += 0  

if salario_bruto > 500:
    parte = salario_bruto - 500
    if parte > 400:
        impuesto += 400 * 0.25
    else:
        impuesto += parte * 0.25

if salario_bruto > 900:
    impuesto += (salario_bruto - 900) * 0.45

salario_neto = salario_bruto - impuesto

print("Trabajador:", nombre)
print("Salario bruto:", salario_bruto, "€")
print("Impuestos:", impuesto, "€")
print("Salario neto:", salario_neto, "€")
