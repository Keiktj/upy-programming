# Ejercicio 10 — Visitas web

def analizar_visitas():
    visitas = []
    print("Ingresa los nombres de usuario que visitaron el sitio (escribe 'fin' para terminar):")
    
    while True:
        usuario = input("Usuario: ").strip().lower()
        if usuario == 'fin':
            break
        if usuario:
            visitas.append(usuario)

    usuarios_unicos = set(visitas)

    print("\n--- Reporte de Visitas Web ---")
    print(f"Total de accesos registrados: {len(visitas)}")
    print(f"Usuarios únicos que visitaron: {len(usuarios_unicos)}")
    print(f"Lista de usuarios únicos: {sorted(list(usuarios_unicos))}")

if __name__ == "__main__":
    analizar_visitas()
