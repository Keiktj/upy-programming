# Ejercicio 4 — Tiempos de carrera

def registrar_tiempos():
    tiempos = []
    print("Ingresa los tiempos de carrera en segundos (escribe 'fin' para terminar):")
    while True:
        entrada = input("Tiempo (segundos): ")
        if entrada.lower() == 'fin':
            break
        try:
            t = float(entrada)
            if t > 0:
                tiempos.append(t)
            else:
                print("El tiempo debe ser mayor a 0.")
        except ValueError:
            print("Entrada no válida.")

    if tiempos:
        print("\n--- Tiempos de Carrera ---")
        print(f"Mejor tiempo (más rápido): {min(tiempos)} s")
        print(f"Peor tiempo (más lento): {max(tiempos)} s")
        print(f"Tiempo promedio: {sum(tiempos) / len(tiempos):.2f} s")

if __name__ == "__main__":
    registrar_tiempos()
