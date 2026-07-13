edad = int(input("Ingresa tu edad: "))
precio_base = float(input("Ingresa el precio base del boleto: "))

if edad < 5:
    precio_final = 0
elif edad < 18:
    precio_final = precio_base * 0.8
elif edad >= 60:
    precio_final = precio_base * 0.5
else:
    precio_final = precio_base

print(f"El precio final del boleto es: ${precio_final:.2f}")
