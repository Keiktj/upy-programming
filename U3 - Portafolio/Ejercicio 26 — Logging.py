# Ejercicio 26 — Logging.py

import logging

# Configuración básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ejecutar_aplicacion():
    logging.info("La aplicación se ha iniciado correctamente.")
    
    try:
        a, b = 10, 0
        logging.info(f"Intentando dividir {a} entre {b}...")
        resultado = a / b
    except ZeroDivisionError:
        logging.error("Se produjo una división por cero durante la ejecución.")
        
    logging.info("La aplicación ha finalizado su proceso.")

if __name__ == "__main__":
    ejecutar_aplicacion()
