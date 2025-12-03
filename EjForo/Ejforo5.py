texto = input("Escribe una cadena: ")
caracter = input("Escribe el carácter a buscar: ")

encontrado = False

for i in texto:
    if i == caracter:
        encontrado = True
        break   

if encontrado:
    print(f"El carácter '{caracter}' está en la cadena.")
else:
    print(f"El carácter '{caracter}' NO está en la cadena.")
