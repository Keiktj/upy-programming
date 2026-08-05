# Ejercicio 13 — Copiar origen.py

def copiar_archivo():
    origen = "origen.txt"
    destino = "copia.txt"
    
    # Crear un archivo de prueba si no existe
    try:
        with open(origen, "a", encoding="utf-8") as f:
            f.write("Contenido de prueba para copiar.\n")
            
        with open(origen, "r", encoding="utf-8") as archivo_origen:
            contenido = archivo_origen.read()
            
        with open(destino, "w", encoding="utf-8") as archivo_destino:
            archivo_destino.write(contenido)
            
        print(f"El contenido de '{origen}' se copió exitosamente en '{destino}'.")
    except FileNotFoundError:
        print(f"El archivo '{origen}' no fue encontrado.")

if __name__ == "__main__":
    copiar_archivo()
