# Ejercicio 2 — Estación meteorológica

def monitorear_temperaturas():
    temperaturas = []
    
    print("Ingresa las temperaturas registradas (escribe 'fin' para terminar):")
    while True:
        entrada = input("Temperatura: ")
        if entrada.lower() == 'fin':
            break
        try:
            temp = float(entrada)
            temperaturas.append(temp)
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número.")

    if temperaturas:
        temp_max = max(temperaturas)
        temp_min = min(temperaturas)
        promedio = sum(temperaturas) / len(temperaturas)
        
        print("\n--- Informe Meteorológico ---")
        print(f"Temperatura Máxima: {temp_max}°C")
        print(f"Temperatura Mínima: {temp_min}°C")
        print(f"Temperatura Promedio: {promedio:.2f}°C")
    else:
        print("No se registraron temperaturas.")

if __name__ == "__main__":
    monitorear_temperaturas()
