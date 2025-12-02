num1 = int(input("Inserte el primer número:"))
num2 = int(input("Inserte el segundo número:"))

if (num1 > num2):
    print(num1, "es mayor que", num2)
elif(num1 == num2):
    print("El primer y segundo número son iguales")
else:
    print(num1,"es menor que", num2)
