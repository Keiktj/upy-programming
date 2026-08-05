# Ejercicio 24 — procesar_pedido.py

def procesar_pedido(cantidad):
    if not isinstance(cantidad, int):
        raise TypeError("La cantidad debe ser un número entero.")
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a cero.")
    print(f"Pedido procesado exitosamente por {cantidad} unidades.")

if __name__ == "__main__":
    try:
        unidades = int(input("Ingresa la cantidad de artículos a pedir: "))
        procesar_pedido(unidades)
    except ValueError as e:
        print(f"Error en el pedido: {e}")
    except TypeError as e:
        print(f"Error de tipo: {e}")
