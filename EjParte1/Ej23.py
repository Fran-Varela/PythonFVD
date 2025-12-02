valor_compra = float(input("Ingrese el valor de la compra: "))
pago = input("Ingrese el tipo de pago (contado/tarjeta): ")

if pago == "contado":
    descuento = valor_compra * 0.05
    total = valor_compra - descuento
    print("Descuento aplicado:", descuento)
    print("Total a pagar:", total)
elif pago == "tarjeta":
    recargo = valor_compra * 0.03
    total = valor_compra + recargo
    print("Recargo aplicado:", recargo)
    print("Total a pagar:", total)
else:
    print("Método de pago no válido")
