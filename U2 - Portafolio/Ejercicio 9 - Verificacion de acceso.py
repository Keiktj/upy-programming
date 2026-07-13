usuario_correcto = "admin"
contrasenia_correcta = "1234"

usuario = input("Usuario: ")
contrasenia = input("Contraseña: ")

if usuario == usuario_correcto and contrasenia == contrasenia_correcta:
    print("Acceso concedido")
else:
    print("Acceso denegado")
