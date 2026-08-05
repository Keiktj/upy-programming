# Ejercicio 21 — Inventario.py

def gestionar_inventario():
    inventario = {"Manzanas": 50, "Pan": 20, "Leche": 15}
    print(f"Inventario actual: {inventario}")
    
    producto = input("Ingresa el nombre del producto que deseas consultar: ").strip().capitalize()
    
    try:
        cantidad = inventario[producto]
        print(f"Stock disponible de {producto}: {cantidad} unidades.")
    except KeyError:
        print(f"Error: El producto '{producto}' no se encuentra en el inventario.")

if __name__ == "__main__":
    gestionar_inventario()
