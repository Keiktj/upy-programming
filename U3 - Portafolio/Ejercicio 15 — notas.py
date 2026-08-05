# Ejercicio 15 — notas.py

def procesar_notas():
    nombre_archivo = "notas.txt"
    
    # Crear archivo de prueba con formato 'Nombre,Nota'
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("Juan,85\nMaria,92\nCarlos,68\nAna,74\n")
        
    try:
        aprobados = []
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                if len(partes) == 2:
                    nombre, nota_str = partes[0], partes[1]
                    if float(nota_str) >= 70:
                        aprobados.append((nombre, nota_str))
                        
        print("--- Alumnos Aprobados (>= 70) ---")
        for alum, nota in aprobados:
            print(f"Estudiante: {alum} | Nota: {nota}")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

if __name__ == "__main__":
    procesar_notas()
