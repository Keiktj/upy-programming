# Ejercicio 20 — ventas.py

def calcular_promedio_ventas():
    nombre_archivo = "ventas.txt"
    
    # Crear archivo de prueba
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("1500.50\n2300.00\n1800.25\n3100.00\n")
        
    try:
        ventas = []
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    ventas.append(float(linea))
                    
        if ventas:
            promedio = sum(ventas) / len(ventas)
            print(f"Ventas registradas: {ventas}")
            print(f"Promedio de ventas: ${promedio:.2f}")
    except FileNotFoundError:
        print(f"No se encontró el archivo '{nombre_archivo}'.")

if __name__ == "__main__":
    calcular_promedio_ventas()
