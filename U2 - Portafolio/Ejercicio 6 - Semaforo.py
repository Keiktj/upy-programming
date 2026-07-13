color = input("Ingresa el color del semáforo (rojo/amarillo/verde): ").lower().strip()

if color == "rojo":
    print("Alto. No puedes avanzar.")
elif color == "amarillo":
    print("Precaución. Disminuye la velocidad o prepárate para parar.")
elif color == "verde":
    print("Siga. Puedes avanzar.")
else:
    print("Color de semáforo no válido.")
