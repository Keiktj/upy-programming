# Ejercicio 23 — Orden.py

def acceder_elemento():
    lista = ["Python", "Java", "C++", "JavaScript", "Go"]
    print(f"Lista de elementos: {lista}")
    
    try:
        indice = int(input("Ingresa un índice (0 a 4): "))
        elemento = lista[indice]
        print(f"El elemento en el índice {indice} es: {elemento}")
    except IndexError:
        print(f"Error: El índice {indice} está fuera de rango para la lista.")
    except ValueError:
        print("Error: Por favor ingresa un número entero.")

if __name__ == "__main__":
    acceder_elemento()
