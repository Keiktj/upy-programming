# Ejercicio 18 — Rutas.py

import os

def verificar_archivo():
    nombre_archivo = input("Ingresa el nombre o ruta del archivo a verificar: ").strip()
    
    if os.path.exists(nombre_archivo):
        print(f"El archivo/ruta '{nombre_archivo}' SÍ existe.")
        if os.path.isfile(nombre_archivo):
            print("Es un archivo.")
        elif os.path.isdir(nombre_archivo):
            print("Es un directorio/carpeta.")
    else:
        print(f"El archivo/ruta '{nombre_archivo}' NO existe.")

if __name__ == "__main__":
    verificar_archivo()
