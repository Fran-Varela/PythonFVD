num1 = int(input("Ingresa el primer número:"))
num2 = int(input("Ingresa el segundo número"))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

try:
    division = num1 / num2
    print("El resultado de la suma es:", suma, "El resultado de la resta es:", resta, "El resultado de la multiplicación es:", multiplicacion, "El resultaqdo de la división es:", division)

except ZeroDivisionError:
    print("No se puede dividir por cero")