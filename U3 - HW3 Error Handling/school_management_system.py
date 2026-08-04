# INPUT
alumnos = []
materias = []
calificaciones = {}

print("--- SISTEMA DE GESTIÓN ESCOLAR (CON MANEJO DE ERRORES) ---")

try:
    # Captura del número de alumnos
    num_alumnos = int(input("¿Cuántos alumnos deseas registrar?: "))
    if num_alumnos <= 0:
        raise ValueError("Debe registrar al menos 1 alumno.")

    for i in range(num_alumnos):
        nombre = input(f"Ingresa el nombre del alumno {i+1}: ").strip()
        if not nombre:
            raise ValueError("El nombre del alumno no puede estar vacío.")
        alumnos.append(nombre)

    # Captura del número de materias
    num_materias = int(input("\n¿Cuántas materias deseas registrar?: "))
    if num_materias <= 0:
        raise ValueError("Debe registrar al menos 1 materia.")

    for j in range(num_materias):
        materia = input(f"Ingresa el nombre de la materia {j+1}: ").strip()
        if not materia:
            raise ValueError("El nombre de la materia no puede estar vacío.")
        materias.append(materia)

    # Captura de calificaciones
    print("\n--- CAPTURA DE CALIFICACIONES ---")
    for alumno in alumnos:
        calificaciones[alumno] = {}
        for materia in materias:
            calif = float(input(f"Calificación de {alumno} en {materia} (0-10): "))
            if calif < 0 or calif > 10:
                raise ValueError("La calificación debe estar entre 0 y 10.")
            calificaciones[alumno][materia] = calif

# PROCESS
    promedios_alumnos = {}
    suma_total_grupo = 0
    total_calificaciones = 0

    for alumno, materias_calif in calificaciones.items():
        suma_alumno = sum(materias_calif.values())
        promedio = suma_alumno / len(materias)
        promedios_alumnos[alumno] = promedio
        
        suma_total_grupo += suma_alumno
        total_calificaciones += len(materias)

    promedio_general_grupo = suma_total_grupo / total_calificaciones if total_calificaciones > 0 else 0

# OUTPUT
    print("\n" + "="*40)
    print("       REPORTE FINAL DEL SISTEMA       ")
    print("="*40)

    for alumno in alumnos:
        print(f"\nAlumno: {alumno}")
        for materia, calif in calificaciones[alumno].items():
            print(f"  - {materia}: {calif}")
        print(f"  --> Promedio general: {promedios_alumnos[alumno]:.2f}")

    print("\n" + "-"*40)
    print(f"PROMEDIO GENERAL DEL GRUPO: {promedio_general_grupo:.2f}")
    print("-"*40)

except ValueError as e:
    print(f"\n[ERROR EN LOS DATOS]: {e}")
except Exception as e:
    print(f"\n[ERROR INESPERADO]: {e}")
