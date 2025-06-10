texto = input("ingresa una cadena de texto: ")

texto = texto.lower()

vocales = "aeiou"

contador_vocales = 0

contador_consonantes = 0

for caracter in texto:
    if caracter.isalpha():
        if caracter in vocales:
            contador_vocales += 1

        else: 
            contador_consonantes += 1

print(f"la cadena contiene {contador_vocales} vocales y {contador_consonantes} consonantes. ")
