opciones = int(input("Birenvenido a su cajero Virtual" 
"1- Ingresar dinero en su cuenta" 
"2 -Retirar dinero de cuenta"
"3- Salir"))

saldo = 1000

if (opciones == 1):
    dinero_ingresado = int(input("¿Cuanto dinero le gustaría ingresar?"))
    nuevosaldo = saldo + dinero_ingresado
    print("Ahora usted tiene", nuevosaldo, "euros en su cuenta")
elif (opciones == 2):
    dinero_retirado = int(input("¿Cuanto dinero le gustaria retirar?"))
    nuevosaldo = saldo - dinero_retirado
    print("Ahora usted tiene", nuevosaldo, "euros en su cuenta")
else: 
    exit()