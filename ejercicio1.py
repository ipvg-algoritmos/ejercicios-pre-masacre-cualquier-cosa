numeros = (11, 22, 33, 44, 55, 66, 77, 88, 99)

numero_buscar = int(input("Ingrese el numero que deseas buscar: "))

if numero_buscar in numeros:
    posicion = numeros.index(numero_buscar)

    print(f"el numero {numero_buscar} se encuentra en la posicion {posicion} de la lista.")

else:
    print(f"el numero {numero_buscar} no se encuentra en la lista")

