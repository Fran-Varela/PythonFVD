num1 = int(input("Ingrese el primer número:"))
num2 = int(input("Ingrese el segundo número:"))
num3 = int(input("Ingrese el tercer número:"))

mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)

if (num1 == num2 and num2 == num3):
    print("Los tres números son iguales")
elif (num1 == num2):
    print("El primer y segundo número son iguales y", mayor, "es el mayor", menor, "es el menor")
elif (num2 == num3):
    print("El tercer y segundo número son iguales y", mayor, "es el mayor", menor, "es el menor")
else:
    print("El numero", mayor, "es mayor y el número", menor, "es menor")
