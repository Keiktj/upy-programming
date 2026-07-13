peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Categoría: Bajo peso")
elif 18.5 <= imc < 25:
    print("Categoría: Peso normal")
elif 25 <= imc < 30:
    print("Categoría: Sobrepeso")
else:
    print("Categoría: Obesidad")
