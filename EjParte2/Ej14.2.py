altura = int(input("Introduce la altura: "))
for i in range(1, altura+1):
    espacios = altura - i
    print(" " * espacios + "*" * (2*i-1))