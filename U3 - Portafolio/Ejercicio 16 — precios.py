# Ejercicio 16 — precios.py

def procesar_precios():
    nombre_archivo = "precios.txt"
    
    # Crear archivo de prueba
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("15.50\n20.00\n5.75\n100.00\n42.10\n")
        
    try:
        precios = []
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    precios.append(float(linea))
                    
        if precios:
            total = sum(precios)
            print(f"Lista de precios: {precios}")
            print(f"Suma total de los precios: ${total:.2f}")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")

if __name__ == "__main__":
    procesar_precios()
