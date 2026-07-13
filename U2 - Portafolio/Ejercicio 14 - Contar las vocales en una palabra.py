palabra = input("Ingresa una palabra o frase: ").lower()
contador_vocales = 0

for caracter in palabra:
    if caracter in 'aeiouáéíóú':
        contador_vocales += 1

print(f"El número de vocales en el texto es: {contador_vocales}")
