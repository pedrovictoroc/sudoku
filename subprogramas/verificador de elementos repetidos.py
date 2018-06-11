# o algoritmo considera apenas matrizes quadradas

# funções

def exibir_matriz(matriz):
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz)):
            print("{} ".format(matriz[i][j]), end="")
        print()

def exibir_matriz_2(matriz):
    # separadores
    linha_letras = "    A   B   C    D   E   F    G   H   I"
    separador = " ++---+---+---++---+---+---++---+---+---++"
    separador2 = " ++===+===+===++===+===+===++===+===+===++"
    print(linha_letras)
    # imprime os separadores e as linhas com elementos da matriz
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
    print(separador)

# preenche a linha especificada da matriz com o valor de 'el'
def preencher_linha_matriz(linha, matriz, el):
    for i in range(0, len(matriz)):
        matriz[linha][i] = el
    return matriz

# preenche cada linha da matriz com números de 1 ao total de elementos da matriz
def preencher_matriz(matriz):
    contador = 0
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz)):
            contador += 1
            matriz[i][j] = contador

# preenche cada linha da matriz com números de 1 a len(matriz)
def preencher_matriz_2(matriz):
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz)):
            matriz[i][j] = j + 1

# preenche cada região de uma matriz 9x9 com números de 1 a 9
def preencher_matriz_3(matriz):
    auxiliar = 0
    auxiliar_2 = 0
    for i in range(0, 9): # um laço para cada região
        contador = 1
        for j in range(auxiliar, auxiliar + 3):
            for k in range(auxiliar_2, auxiliar_2 + 3):
                matriz[j][k] = contador
                contador += 1
        auxiliar_2 += 3
        if (i + 1) % 3 == 0:
            auxiliar += 3
            auxiliar_2 = 0

def inserir_valor(linha, coluna, valor, matriz):
    matriz[linha][coluna] = valor

def verificar_linha_repetida(matriz):
    for i in range(0, len(matriz)):
        validacao = True
        for j in range(0, len(matriz)):
            for k in range(j+1, len(matriz)):
                if matriz[i][k] == matriz[i][j]:
                    validacao = False
                    print("{} esta repetido na linha {} e coluna {}".format(matriz[i][k], i, j))

def verificar_coluna_repetida(matriz):
    for i in range(0, len(matriz)):
            validacao = True
            for j in range(0, len(matriz)):
                for k in range(j+1, len(matriz)):
                    if matriz[k][i] == matriz[j][i]:
                        validacao = False
                        print("{} esta repetido na linha {} e coluna {}".format(matriz[k][i], k, i))

# considerando uma matriz 9x9
def verificar_regiao_repetida(matriz): # cada índice representa uma número da região
    validacao_1 = True
    auxiliar = 0
    auxiliar_2 = 0
    for i in range(0, 9): # um laço para cada região
        validacao_2 = [0] * 10
        for j in range(auxiliar, auxiliar + 3):
            for k in range(auxiliar_2, auxiliar_2 + 3):
                validacao_2[matriz[j][k]] += 1
        for l in range(1, 10): # verifica se há elementos repetidos na região
            if validacao_2[l] > 1:
                print("Elemento {} repetido na regiao {}".format(l, i + 1))
                validacao_1 = False
        auxiliar_2 += 3
        if (i + 1) % 3 == 0:
            auxiliar += 3
            auxiliar_2 = 0
    return validacao_1
            

# algoritmo principal
matriz = [["*"] * 9 for i in range(9)] # '*' representa uma posição sem elemento algum

# debug
preencher_matriz_3(matriz)
while True:
    exibir_matriz_2(matriz)
    print("Insira linha, coluna e valor: ")
    linha, coluna, valor = input().split()
    print(linha, coluna, valor)
    linha, coluna, valor = int(linha), int(coluna), int(valor)
    inserir_valor(linha, coluna, valor, matriz)
    verificar_linha_repetida(matriz) # funcionando
    verificar_coluna_repetida(matriz) # funcionando
    print("True para nao repeticao na regiao, False para repeticao:")
    print(verificar_regiao_repetida(matriz)) #funcionando
