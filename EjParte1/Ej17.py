nombre_usuario = input("Introduzca su nombre de usuario:")
contraseña = input("Introduzca su contraseña:")

print("Bienvenido al Inicio de sesión")

inicio_sesion_usuario = input("Nombre de usuario:")
inicio_sesion_contraseña = input("Contraseña:")

if (nombre_usuario == inicio_sesion_usuario and contraseña == inicio_sesion_contraseña):
    print("Nombre y contraseña correctos, Bienvenido al sistema")
else:
    print("Nombre o usuario incorrectos, vuelva a intentarlo")