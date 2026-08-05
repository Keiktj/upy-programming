# Ejercicio 3 — Sensor

def registrar_lecturas():
    lecturas = []
    limite = 5
    
    print(f"Ingresa {limite} lecturas del sensor:")
    for i in range(1, limite + 1):
        while True:
            try:
                valor = float(input(f"Lectura {i}: "))
                lecturas.append(valor)
                break
            except ValueError:
                print("Valor inválido. Por favor, ingresa un número.")
                
    print("\n--- Resultados del Sensor ---")
    print(f"Lecturas registradas: {lecturas}")
    print(f"Valor máximo: {max(lecturas)}")
    print(f"Valor mínimo: {min(lecturas)}")
    print(f"Promedio de lecturas: {sum(lecturas) / len(lecturas):.2f}")

if __name__ == "__main__":
    registrar_lecturas()
