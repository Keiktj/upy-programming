# Ejercicio 22 — Operaciones.py

def realizar_division():
    print("=== Calculadora de División ===")
    try:
        num1 = float(input("Ingresa el primer número (dividendo): "))
        num2 = float(input("Ingresa el segundo número (divisor): "))
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")
    except ValueError:
        print("Error: Debes ingresar números válidos.")

if __name__ == "__main__":
    realizar_division()
