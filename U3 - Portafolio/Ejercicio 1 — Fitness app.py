# Ejercicio 1 — Fitness app

def registrar_pasos():
    pasos_semana = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    for dia in dias:
        monto = int(input(f"Ingresa los pasos del {dia}: "))
        pasos_semana.append(monto)
        
    total_pasos = sum(pasos_semana)
    promedio_pasos = total_pasos / len(pasos_semana)
    dia_max = dias[pasos_semana.index(max(pasos_semana))]
    dia_min = dias[pasos_semana.index(min(pasos_semana))]
    
    print("\n--- Resumen de la Semana ---")
    print(f"Total de pasos: {total_pasos}")
    print(f"Promedio diario: {promedio_pasos:.2f}")
    print(f"Día con más pasos: {dia_max} ({max(pasos_semana)})")
    print(f"Día con menos pasos: {dia_min} ({min(pasos_semana)})")

if __name__ == "__main__":
    registrar_pasos()
