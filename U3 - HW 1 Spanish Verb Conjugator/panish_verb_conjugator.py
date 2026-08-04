# INPUT
verbo = input("Ingresa un verbo regular en infinitivo (ej. hablar, comer, vivir): ").strip().lower()
print("\nSelecciona el modo/tiempo verbal:")
print("1: Presente")
print("2: Pretérito (Pasado)")
print("3: Futuro")
modo = input("Opción (1, 2 o 3): ").strip()

# PROCESS
raiz = verbo[:-2]
terminacion = verbo[-2:]

pronombres = ["Yo", "Tú", "Él/Ella/Usted", "Nosotros/as", "Vosotros/as", "Ellos/Ellas/Ustedes"]

sufijos = {
    "ar": {
        "1": ["o", "as", "a", "amos", "áis", "an"],
        "2": ["é", "aste", "ó", "amos", "asteis", "aron"],
        "3": ["aré", "arás", "ará", "aremos", "aréis", "arán"]
    },
    "er": {
        "1": ["o", "es", "e", "emos", "éis", "en"],
        "2": ["í", "iste", "ió", "imos", "isteis", "ieron"],
        "3": ["eré", "erás", "erá", "eremos", "eréis", "erán"]
    },
    "ir": {
        "1": ["o", "es", "e", "imos", "ís", "en"],
        "2": ["í", "iste", "ió", "imos", "isteis", "ieron"],
        "3": ["iré", "irás", "irá", "iremos", "iréis", "irán"]
    }
}

resultados = []

if terminacion in sufijos and modo in ["1", "2", "3"]:
    for i in range(len(pronombres)):
        if modo == "3":
            conjugado = f"{verbo}{sufijos[terminacion]['3'][i][2:]}"
        else:
            conjugado = f"{raiz}{sufijos[terminacion][modo][i]}"
        resultados.append(f"{pronombres[i]} {conjugado}")
else:
    resultados.append("Verbo o modo no válido.")

# OUTPUT
print("\n--- RESULTADOS DE CONJUGACIÓN ---")
for linea in resultados:
    print(linea)
