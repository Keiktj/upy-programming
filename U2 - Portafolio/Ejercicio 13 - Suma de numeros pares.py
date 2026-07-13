n = int(input("Ingresa un número entero positivo N: "))

if n > 0:
    suma_pares = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            suma_pares += i
    print(f"La suma de los números pares desde 1 hasta {n} es: {suma_pares}")
else:
    print("Por favor, ingresa un número positivo.")
