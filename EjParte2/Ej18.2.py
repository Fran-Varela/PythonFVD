A = int(input("Introduce A: "))
B = int(input("Introduce B: "))
resultado = 1
for i in range(B):
    resultado *= A
print(A, "elevado a", B, "es:", resultado)