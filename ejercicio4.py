numeros = []
while True:
    n = float(input("ingrese un numero (negativo para terminar): "))
    if n < 0:
        break
    numeros.append(n)

if numeros:
    promedio = sum(numeros) / len(numeros)
    print("el promedio es:", promedio)
else:
    print("no se ingresaron numeros validos.")