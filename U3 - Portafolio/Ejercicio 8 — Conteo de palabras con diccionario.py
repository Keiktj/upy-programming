# Ejercicio 8 — Conteo de palabras con diccionario

def contar_palabras():
    texto = input("Ingresa un texto o frase: ").strip().lower()
    
    # Limpiar signos de puntuación básicos
    for simbolo in [".", ",", ";", ":", "!", "?", "¡", "¿"]:
        texto = texto.replace(simbolo, "")
        
    palabras = texto.split()
    frecuencias = {}

    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    print("\n--- Frecuencia de Palabras ---")
    for palabra, conteo in frecuencias.items():
        print(f"'{palabra}': {conteo}")

if __name__ == "__main__":
    contar_palabras()
