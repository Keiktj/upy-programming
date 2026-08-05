# Ejercicio 19 — empleados.py

def buscar_empleado():
    nombre_archivo = "empleados.txt"
    
    # Crear archivo de prueba
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("Carlos Gomez, Desarrollador\nAna Lopez, Diseñadora\nLuis Perez, Contador\n")
        
    busqueda = input("Ingresa el nombre del empleado a buscar: ").strip().lower()
    encontrado = False
    
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if busqueda in linea.lower():
                    print(f"Empleado encontrado: {linea.strip()}")
                    encontrado = True
                    break
        if not encontrado:
            print("Empleado no registrado.")
    except FileNotFoundError:
        print(f"No se encontró el archivo '{nombre_archivo}'.")

if __name__ == "__main__":
    buscar_empleado()
