numeros = []
while True:
    n = int(input("ingrese un numero (negativo para terminar): "))
    if n < 0:
        break
    numeros.append(n)

if numeros:
    print("el numero mayor es:", max(numeros))
    print("el numero menor es:", min(numeros))
else:
    print("no se ingresaron numeros validos.")
    