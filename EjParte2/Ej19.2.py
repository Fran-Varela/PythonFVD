print("Piensa un número del 1 al 100")
bajo = 1
alto = 100
encontrado = False

while not encontrado:
    intento = (bajo + alto) // 2
    print("¿Es", intento, "?")
    respuesta = input("Responde mayor, menor o igual: ")
    if respuesta == "igual":
        print("¡Adiviné!")
        encontrado = True
    elif respuesta == "mayor":
        bajo = intento + 1
    elif respuesta == "menor":
        alto = intento - 1