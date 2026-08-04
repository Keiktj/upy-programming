# INPUT
# Datos iniciales para la gestión escolar
alumnos = []
materias = []
calificaciones = {}

print("--- SISTEMA DE GESTIÓN ESCOLAR ---")

# Registro de número de alumnos
num_alumnos = int(input("¿Cuántos alumnos deseas registrar?: "))
for i in range(num_alumnos):
    nombre = input(f"Ingresa el nombre del alumno {i+1}: ").strip()
    alumnos.append(nombre)

# Registro de número de materias
num_materias = int(input("\n¿Cuántas materias deseas registrar?: "))
for j in range(num_materias):
    materia = input(f"Ingresa el nombre de la materia {j+1}: ").strip()
    materias.append(materia)

# Captura de calificaciones
print("\n--- CAPTURA DE CALIFICACIONES ---")
for alumno in alumnos:
    calificaciones[alumno] = {}
    for materia in materias:
        calif = float(input(f"Calificación de {alumno} en {materia}: "))
        calificaciones[alumno][materia] = calif


# PROCESS
# Cálculo de promedios por alumno y del grupo
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
# Muestra de resultados finales
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
