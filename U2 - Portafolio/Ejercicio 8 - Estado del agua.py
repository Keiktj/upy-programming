temperatura = float(input("Ingresa la temperatura del agua en °C: "))

if temperatura <= 0:
    print("Estado: Sólido (Hielo)")
elif 0 < temperatura < 100:
    print("Estado: Líquido")
else:
    print("Estado: Gaseoso (Vapor)")
