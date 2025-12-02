nombre = input("Ingrese el nombre del postulante: ")
facultad = input("Ingrese la facultad: ")

if facultad == "ingenieria":
    importe = 500
    mensualidad = 800
elif facultad == "medicina":
    importe = 800
    mensualidad = 1000
elif facultad == "derecho":
    importe = 400
    mensualidad = 600
elif facultad == "arquitectura":
    importe = 600
    mensualidad = 900
else:
    importe = 0
    mensualidad = 0
    print("Facultad no registrada")

if importe > 0:
    igv = (importe + mensualidad) * 0.18
    total = importe + mensualidad + igv
    print("Postulante:", nombre)
    print("Facultad:", facultad)
    print("Importe:", importe)
    print("Mensualidad:", mensualidad)
    print("IGV (18%):", igv)
    print("Monto final a pagar:", total)
