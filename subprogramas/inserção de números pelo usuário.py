import time

validacao = True
matriz = [[""] * 9 for i in range(9)]
letras = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7, "I" : 8, "a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7, "i" : 8}

while validacao:

    coluna = ""
    linha = ""
    valor = ""
    print("Entre uma jogada:")
    jogada = input()

    tempo_inicio = time.clock()

    for i in range(0, len(jogada)):
        if jogada[i].isalpha(): # verifica se o caractere é uma letra
            if jogada[i] in letras:
                coluna = letras[jogada[i]]
        if linha == "":
            if jogada[i].isdigit(): # verifica se o caractere é um número
                linha = int(jogada[i]) - 1
        elif valor == "":
            if jogada[i].isdigit():
                valor = int(jogada[i])
    if coluna != "" and linha != "" and valor != "":
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

    # verifica se a matriz está completa
    contador = 0
    for i in range(0, 9):
        for j in range(0, 9):
            if matriz[i][j] != "":
                contador += 1
    if contador == 81:
        print("Parabens! O sudoku esta completo!")
        validacao = False

    print("A operacao demorou {}s".format(time.clock() - tempo_inicio)) # cálculo do tempo de execução de cada looṕ