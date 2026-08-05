# Ejercicio 9 — Dos encuestas

def comparar_encuestas():
    print("Ingresa los encuestados del Grupo A (separados por coma):")
    grupo_a = set([nombre.strip().capitalize() for nombre in input().split(",") if nombre.strip()])
    
    print("\nIngresa los encuestados del Grupo B (separados por coma):")
    grupo_b = set([nombre.strip().capitalize() for nombre in input().split(",") if nombre.strip()])

    print("\n--- Resultados de Conjuntos ---")
    print(f"Personas en ambas encuestas: {list(grupo_a.intersection(grupo_b))}")
    print(f"Todas las personas únicas (Unión): {list(grupo_a.union(grupo_b))}")
    print(f"Solo en Grupo A: {list(grupo_a.difference(grupo_b))}")
    print(f"Solo en Grupo B: {list(grupo_b.difference(grupo_a))}")

if __name__ == "__main__":
    comparar_encuestas()
