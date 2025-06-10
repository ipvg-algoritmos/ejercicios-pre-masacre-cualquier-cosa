numeros = []
while True:
    n = int(input("Ingrese un número (negativo para terminar): "))
    if n < 0:
        break
    numeros.append(n)

if numeros:
    print("El número mayor es:", max(numeros))
    print("El número menor es:", min(numeros))
else:
    print("No se ingresaron números válidos. ")