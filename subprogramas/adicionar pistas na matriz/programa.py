# lê o arquivo "pistas.txt" e atribui à variável pistas
arquivo = open("pistas.txt", "r")
pistas = arquivo.read()
arquivo.close()

# grava as pistas na matriz
matriz = [[""] * 9 for i in range(9)]
letras = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7, "I" : 8}
for i in range(0, len(pistas)):
    if pistas[i] == ",":
        if pistas[i - 1] in letras:
            coluna = letras[pistas[i - 1]]
            # verificação de linha e coluna aqui
            linha = int(pistas[i + 1]) - 1
            valor = int(pistas[i + 3])
            matriz[linha][coluna] = valor

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

# validação das pistas
validacao = True
if len(pistas) < 5 or len(pistas) > 479: # 6 caracteres por linha, incluindo o '\n'
    validacao = False
if not validacao:
    print("Grade invalida!")