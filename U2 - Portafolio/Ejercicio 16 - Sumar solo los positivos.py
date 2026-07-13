suma_positivos = 0

print("Ingresa números (ingresa 0 para terminar):")
while True:
    numero = float(input("Número: "))
    if numero == 0:
        break
    if numero < 0:
        continue
    suma_positivos += numero

print(f"La suma de los números positivos ingresados es: {suma_positivos}")
