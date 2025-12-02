altura = int(input("Introduce la altura: "))
for i in range(altura, 0, -1):
    espacios = altura - i
    print(" " * espacios + "*" * (2*i-1))