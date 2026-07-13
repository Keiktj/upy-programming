letra = input("Ingresa una letra: ").lower()

if len(letra) == 1 and letra.isalpha():
    if letra in 'aeiou':
        print(f"'{letra}' es una vocal.")
    else:
        print(f"'{letra}' es una consonante.")
else:
    print("Por favor, ingresa solo una letra válida.")
