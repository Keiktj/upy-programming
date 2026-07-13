inicio = int(input("Ingresa el inicio del rango: "))
fin = int(input("Ingresa el fin del rango: "))

encontrado = False

for i in range(inicio, fin + 1):
    if i % 7 == 0:
        print(f"El primer múltiplo de 7 encontrado en el rango es: {i}")
        encontrado = True
        break

if not encontrado:
    print("No se encontraron múltiplos de 7 en ese rango.")
