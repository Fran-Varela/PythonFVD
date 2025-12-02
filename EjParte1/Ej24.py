monto = float(input("Ingrese el monto de la compra: "))
dia = input("Ingrese el día de la semana: ")

if dia == "martes" or dia == "jueves":
    descuento = monto * 0.15
    total = monto - descuento
    print("Descuento aplicado:", descuento)
    print("Total a pagar:", total)
else:
    print("No hay descuento")
    print("Total a pagar:", monto)
