# Ejercicio 14 — temperaturas.py

def procesar_temperaturas():
    nombre_archivo = "temperaturas.txt"
    
    # Crear archivo de prueba
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("22.5\n24.0\n19.8\n25.3\n21.0\n")
        
    try:
        temperaturas = []
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    temperaturas.append(float(linea))
                    
        if temperaturas:
            promedio = sum(temperaturas) / len(temperaturas)
            print(f"Temperaturas registradas: {temperaturas}")
            print(f"Promedio de temperaturas: {promedio:.2f}°C")
    except FileNotFoundError:
        print(f"No se encontró el archivo '{nombre_archivo}'.")

if __name__ == "__main__":
    procesar_temperaturas()
