# Ejercicio 11 — Catálogo de libros

def catalogo_libros():
    catalogo = []
    
    print("=== Registro de Catálogo de Libros ===")
    while True:
        titulo = input("Título del libro (o 'fin' para terminar): ").strip()
        if titulo.lower() == 'fin':
            break
        autor = input(f"Autor de '{titulo}': ").strip()
        try:
            anio = int(input(f"Año de publicación de '{titulo}': "))
            catalogo.append({"titulo": titulo, "autor": autor, "anio": anio})
        except ValueError:
            print("Año inválido. Registro cancelado para este libro.")

    print("\n--- CATÁLOGO REGISTRADO ---")
    for libro in catalogo:
        print(f"Título: {libro['titulo']} | Autor: {libro['autor']} | Año: {libro['anio']}")

if __name__ == "__main__":
    catalogo_libros()
