# Ejercicio 12 — registro.py

def guardar_registro():
    nombre_archivo = "registro_visitas.txt"
    print("Ingresa nombres para registrar en el archivo (escribe 'fin' para salir):")
    
    with open(nombre_archivo, "a", encoding="utf-8") as archivo:
        while True:
            nombre = input("Nombre: ").strip()
            if nombre.lower() == 'fin':
                break
            if nombre:
                archivo.write(nombre + "\n")
                
    print(f"\nDatos guardados exitosamente en '{nombre_archivo}'.")

if __name__ == "__main__":
    guardar_registro()
