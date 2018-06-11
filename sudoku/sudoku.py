# UFC - Universidade Federal do Ceará
# aluno 1, matrícula
# aluno 2, matrícula
# aluno 3, matrícula
# python3

# funções
def exibir_matriz(matriz):
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

def ler_arquivo_texto(nome_arquivo):
    # abre o arquivo em modo leitura
    arquivo = open(nome_arquivo, "r")
    # atribui o conteúdo do arquivo para 'texto'
    texto = arquivo.read()
    arquivo.close()
    return texto

def gravar_pistas(pistas, matriz):
    letras = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7, "I" : 8}
    for i in range(0, len(pistas)):
        if pistas[i] == ",":
            coluna = letras[pistas[i - 1]]
            linha = int(pistas[i + 1]) - 1
            valor = int(pistas[i + 3])
            matriz[linha][coluna] = valor

def verificar_quantidade_pistas(pistas):
    validacao = True
    # verifica se a quantidade de pistas está no intervalo [1, 80]
    if len(pistas) < 5 or len(pistas) > 479: # 6 caracteres por linha, incluindo o '\n'
        validacao = False
        print("Quantidade de pistas invalida")
    return validacao

def tratar_jogada(jogada):
    # remove os espaços da jogada
    jogada = jogada.split()
    jogada = ''.join(jogada)
    # deixa todas as letras maiúsculas
    jogada = jogada.upper()
    return jogada

def verificar_jogada(jogada):
    letras = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7, "I" : 8}
    validacao = True
    if len(jogada) == 5:
        # verifica se o valor da coluna é uma letra e se é uma letra válida
        if jogada[0].isalpha() and jogada[0] in letras:
            coluna = jogada[0]
        else:
            print("Coluna invalida")
            validacao = False

        if jogada[1] != ',' or jogada[3] != ':':
            print("Formato incorreto de jogada")
            validacao = False

        # verifica se o valor da linha é um número
        if jogada[2].isdigit() and (not jogada[3].isdigit()):
            # verifica se o valor da linha pertence ao intervalo permitido
            if int(jogada[2]) > 0 and int(jogada[2]) < 10:
                linha = int(jogada[2])
            else:
                print("Linha invalida")
                validacao = False
        else:
            print("Linha invalida")
            validacao = False

        # verifica se o valor que irá para a matriz é um número
        if jogada[4].isdigit() and len(jogada) == 5:
            # verifica se o valor do número pertence ao intervalo permitido
            if int(jogada[4]) > 0 and int(jogada[4]) < 10:
                numero = int(jogada[4])
            else:
                print("Numero invalido")
                validacao = False
        else:
            print("Numero invalido")
            validacao = False

    else:
        print("Formato incorreto de jogada")
        validacao = False

    return validacao

def apagar_jogada(linha, coluna, matriz):
    matriz[linha][coluna] = ""

def verificar_matriz(matriz):
    validacao = True
    letras = {0 : "A", 1 : "B", 2 : "C", 3 : "D", 4 : "E", 5 : "F", 6 : "G", 7 : "H", 8 : "I"}
    for i in range(0, 9):
        for j in range(0, 9):
            for k in range(j+1, 9):
                if matriz[i][j] != "" and matriz[j][i] != "":
                    # verifica se há números repetidos na linha
                    if matriz[i][k] == matriz[i][j]:
                        validacao = False
                        print("{} esta repetido na linha {}".format(matriz[i][k], i + 1))
                    # verifica se há números repetidos na coluna
                    if matriz[k][i] == matriz[j][i]:
                        validacao = False
                        print("{} esta repetido na coluna {}".format(matriz[k][i], letras[k]))

    """
    # verifica se há números repetidos em cada coluna # remover
    for i in range(0, 9):
        for j in range(0, 9):
            for k in range(j+1, 9):
                if matriz[k][i] == matriz[j][i]:
                    validacao = False
                    print("{} esta repetido na linha {} e coluna {}".format(matriz[k][i], k, i))
    """

    # verifica se há números repetidos em cada região
    auxiliar = 0
    auxiliar_2 = 0
    for i in range(0, 9): # um laço para cada região
        validacao_2 = [0] * 10
        for j in range(auxiliar, auxiliar + 3):
            for k in range(auxiliar_2, auxiliar_2 + 3):
                if matriz[j][k] != "":
                    validacao_2[matriz[j][k]] += 1
        for l in range(1, 10): # verifica se há elementos repetidos na região
            if validacao_2[l] > 1:
                print("{} repetido esta na regiao {}".format(l, i + 1))
                validacao = False
        auxiliar_2 += 3
        if (i + 1) % 3 == 0:
            auxiliar += 3
            auxiliar_2 = 0

    return validacao

def verificar_matriz_completa(matriz):
    validacao = True
    contador = 0
    for i in range(0, 9):
        for j in range(0, 9):
            if matriz[i][j] != "": # atribui +1 ao contador sempre que a posição não estiver vazia
                contador += 1
    if contador == 81:
        validacao = False
    return validacao

def inserir_jogada(jogada, matriz):
    letras = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7, "I" : 8, "a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7, "i" : 8}
    coluna = letras[jogada[0]]
    linha = int(jogada[2]) - 1
    valor = int(jogada[4])
    matriz[linha][coluna] = valor

# algoritmo principal
matriz = [[""] * 9 for i in range(9)]
print("Sudoku\nBem vindo! Digite uma opcao e tecle 'Enter':\n1) Modo Interativo\n2) Modo Batch")
selecao = int(input())

# modo interativo
if selecao == 1:

    letras = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7, "I" : 8, "a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7, "i" : 8} # dicionário para as colunas da matriz
    print("Voce selecionou 'Modo Interativo'")
    pistas = ler_arquivo_texto("pistas.txt")

    if verificar_quantidade_pistas(pistas): # verifica se a quantidade de pistas está no intervalo [1,80]
        gravar_pistas(pistas, matriz)
        if verificar_matriz(matriz):
            matriz_pistas = matriz
            exibir_matriz(matriz)
            while verificar_matriz_completa(matriz): # verifica se a matriz está completa
                print("Entre uma jogada no formato <COL>,<LIN>: <NUMERO>:")
                jogada = input()
                jogada = tratar_jogada(jogada) # deixa a jogada no formato correto
                if verificar_jogada(jogada): # verifica se a jogada é válida
                    if matriz[int(jogada[2]) - 1][letras[jogada[0]]] == "": # verifica se o usuário está tentando sobrescrever uma pista
                        inserir_jogada(jogada, matriz)
                        if verificar_matriz(matriz):
                            exibir_matriz(matriz)
                            if verificar_matriz_completa:
                                print("Parabens! Voce terminou o Sudoku!")
                        else:
                            print("Jogada invalida, entre uma nova jogada:")
                            apagar_jogada(int(jogada[2]) - 1, letras[jogada[0]], matriz)
                    else:
                        print("Jogada inválida. Impossível sobrescrever uma pista. (!)")
                else:
                    print("Jogada invalida, entre uma nova jogada:")
        else:
            print("Entradas inválidas")
    else:
        print("Entradas invalidas")

# modo batch
elif selecao == 2:
    print("Voce selecionou 'Modo Batch'")

else:
    print("Entrada invalida, tente novamente (!)")

# debug