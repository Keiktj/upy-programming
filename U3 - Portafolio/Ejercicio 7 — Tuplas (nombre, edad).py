# Ejercicio 7 — Tuplas (nombre, edad)

def gestionar_personas():
    personas = []
    print("Ingresa nombre y edad (escribe 'fin' en nombre para terminar):")
    
    while True:
        nombre = input("Nombre: ").strip()
        if nombre.lower() == 'fin':
            break
        try:
            edad = int(input(f"Edad de {nombre}: "))
            personas.append((nombre, edad))
        except ValueError:
            print("Edad inválida. Intenta de nuevo.")

    if personas:
        print("\n--- Registro de Personas ---")
        for p in personas:
            print(f"Nombre: {p[0]}, Edad: {p[1]}")
        
        mayores_edad = [p for p in personas if p[1] >= 18]
        print(f"\nTotal de personas mayores de edad: {len(mayores_edad)}")

if __name__ == "__main__":
    gestionar_personas()
