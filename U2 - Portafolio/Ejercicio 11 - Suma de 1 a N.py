n = int(input("Ingresa un número entero positivo N: "))

if n > 0:
    suma = 0
    for i in range(1, n + 1):
        suma += i
    print(f"La suma de los números de 1 hasta {n} es: {suma}")
else:
    print("Por favor, ingresa un número mayor a 0.")
