# Ejercicio 4 — Calificaciones

def gestionar_calificaciones():
    calificaciones = []
    
    print("Ingresa las calificaciones de los estudiantes (escribe 'fin' para terminar):")
    while True:
        entrada = input("Calificación: ")
        if entrada.lower() == 'fin':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 100:
                calificaciones.append(nota)
            else:
                print("Por favor, ingresa una calificación entre 0 y 100.")
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número.")

    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        aprobados = len([c for c in calificaciones if c >= 70])
        reprobados = len(calificaciones) - aprobados
        
        print("\n--- Informe de Calificaciones ---")
        print(f"Total de estudiantes: {len(calificaciones)}")
        print(f"Promedio del grupo: {promedio:.2f}")
        print(f"Aprobados (>= 70): {aprobados}")
        print(f"Reprobados (< 70): {reprobados}")
        print(f"Calificación más alta: {max(calificaciones)}")
        print(f"Calificación más baja: {min(calificaciones)}")
    else:
        print("No se registraron calificaciones.")

if __name__ == "__main__":
    gestionar_calificaciones()
