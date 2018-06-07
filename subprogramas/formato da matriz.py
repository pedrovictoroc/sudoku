import time
tempo_inicio = time.clock()

linha_letras = "    A   B   C    D   E   F    G   H   I"
separador = " ++---+---+---++---+---+---++---+---+---++"
separador2 = " ++===+===+===++===+===+===++===+===+===++"
matriz = [[""] * 9 for i in range(9)]

for i in range(0, 9):
    matriz[i][i] = i+1

# mostrar
print(linha_letras)
for i in range(0, 9):
    if i == 3 or i == 6:
        print(separador2)
    else:
        print(separador)
    print("{}||".format(i+1), end="")
    for j in range(0, 9):
        if matriz[i][j] == "":
            print("   |".format(matriz[i][j]), end="")
        else:
            print(" {} |".format(matriz[i][j]), end="")
        if j == 2 or j == 5:
            print("|", end="")
    print("|{}".format(i+1))
print(linha_letras)

print("Tempo necessario para gerar a matriz: {}s".format(time.clock() - tempo_inicio))