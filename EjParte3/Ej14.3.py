num = int(input("Introduce un número de dos cifras: "))
decenas = num // 10
unidades = num % 10
invertido = unidades * 10 + decenas
print("Número invertido:", invertido)