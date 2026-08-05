# Ejercicio 25 — StockInsuficienteError.py

class StockInsuficienteError(Exception):
    """Excepción personalizada para cuando el stock no es suficiente."""
    def __init__(self, mensaje="Stock insuficiente para completar la venta."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def realizar_venta(stock_actual, cantidad_solicitada):
    if cantidad_solicitada > stock_actual:
        raise StockInsuficienteError(f"Se solicitaron {cantidad_solicitada} unidades, pero solo hay {stock_actual} en stock.")
    return stock_actual - cantidad_solicitada

if __name__ == "__main__":
    stock = 10
    solicitud = 15
    try:
        print(f"Intentando vender {solicitud} unidades con stock de {stock}...")
        stock_restante = realizar_venta(stock, solicitud)
        print(f"Venta realizada. Stock restante: {stock_restante}")
    except StockInsuficienteError as e:
        print(f"Excepción capturada: {e}")
