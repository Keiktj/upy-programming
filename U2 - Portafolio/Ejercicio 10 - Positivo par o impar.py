numero = int(input("Ingresa un número entero: "))

if numero > 0:
    if numero % 2 == 0:
        print(f"El número {numero} es positivo y par.")
    else:
        print(f"El número {numero} es positivo e impar.")
elif numero < 0:
    print(f"El número {numero} es negativo.")
else:
    print("El número es cero.")
