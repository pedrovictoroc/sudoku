# lê o arquivo "pistas.txt" e atribui à variável pistas
arquivo = open("pistas.txt", "r")
pistas = arquivo.read()
arquivo.close()

# grava as pistas na matriz
matriz = [[""] * 9 for i in range(9)]
"""
for i in range(0, 9):
    for j in range(0, 9):
        matriz[i][j]
"""

# exibe a matriz na tela no formato correto
linha_letras = "    A   B   C    D   E   F    G   H   I"
separador = " ++---+---+---++---+---+---++---+---+---++"
separador2 = " ++===+===+===++===+===+===++===+===+===++"
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
