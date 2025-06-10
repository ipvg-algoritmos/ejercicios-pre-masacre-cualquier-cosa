matriz = []
positivos = negativos = ceros = 0

print("Ingrese los valores para una matriz 3x3: ")

for i in range(3):
    fila = []
    for j in range(3):
        valor = int(input(f"Ingrese el valor para la posicion [{i}][{j}]: "))
        fila.append(valor)
        if valor > 0:
            positivos += 1
        elif valor < 0: 
            negativos += 1
        else:
            ceros += 1
    matriz.append(fila)

suma_diag_principal = 0
suma_diag_secundaria = 0

for i in range(3):
    suma_diag_principal = sum(matriz[i][i] for i in range(3))
    suma_diag_secundaria = sum(matriz[i][2 - i] for i in range(3))

print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)
print("Cantidad de ceros:", ceros)

if suma_diag_principal > suma_diag_secundaria: 
    print("la suma de la diagonal principal es es mayor que la secundaria.")
elif suma_diag_principal < suma_diag_secundaria:
    print("la suma de la diagonal principal es menor que la secundaria.")
else:
    print("las sumas de ambas diagonales son iguales.")
