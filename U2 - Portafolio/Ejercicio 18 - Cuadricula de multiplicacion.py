n = int(input("Ingresa el tamaño de la cuadrícula (N): "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end="\t")
    print()
