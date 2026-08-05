# Ejercicio 17 — numeros.py

def filtrar_pares():
    nombre_archivo = "numeros.txt"
    
    # Crear archivo de prueba
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n")
        
    try:
        pares = []
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea and int(linea) % 2 == 0:
                    pares.append(int(linea))
                    
        print(f"Números pares encontrados en '{nombre_archivo}': {pares}")
    except FileNotFoundError:
        print(f"No se encontró el archivo '{nombre_archivo}'.")

if __name__ == "__main__":
    filtrar_pares()
