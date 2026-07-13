valor = float(input("Ingresa un valor: "))
minimo = float(input("Ingresa el límite mínimo del rango: "))
maximo = float(input("Ingresa el límite máximo del rango: "))

if minimo <= valor <= maximo:
    print(f"El valor {valor} está dentro del rango [{minimo}, {maximo}].")
else:
    print(f"El valor {valor} está fuera del rango.")
