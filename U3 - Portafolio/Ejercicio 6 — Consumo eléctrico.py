# Ejercicio 6 — Consumo eléctrico

def analizar_consumo():
    consumos = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    print("Ingresa el consumo eléctrico diario en kWh:")
    for dia in dias:
        while True:
            try:
                kwh = float(input(f"Consumo {dia}: "))
                if kwh >= 0:
                    consumos.append(kwh)
                    break
                else:
                    print("El consumo no puede ser negativo.")
            except ValueError:
                print("Entrada no válida.")

    total_kwh = sum(consumos)
    promedio_kwh = total_kwh / len(consumos)
    
    print("\n--- Reporte de Consumo Eléctrico ---")
    print(f"Consumo total de la semana: {total_kwh:.2f} kWh")
    print(f"Consumo promedio diario: {promedio_kwh:.2f} kWh")
    print(f"Día de mayor consumo: {dias[consumos.index(max(consumos))]} ({max(consumos)} kWh)")
    print(f"Día de menor consumo: {dias[consumos.index(min(consumos))]} ({min(consumos)} kWh)")

if __name__ == "__main__":
    analizar_consumo()
