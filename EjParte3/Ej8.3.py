sueldo_base = float(input("Introduce el sueldo base: "))
venta1 = float(input("Introduce el valor de la primera venta: "))
venta2 = float(input("Introduce el valor de la segunda venta: "))
venta3 = float(input("Introduce el valor de la tercera venta: "))
comision = (venta1 + venta2 + venta3) * 0.10
total = sueldo_base + comision
print("Comisión:", comision)
print("Total a recibir:", total)