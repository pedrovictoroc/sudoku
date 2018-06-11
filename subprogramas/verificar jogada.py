while True:
    letras = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7, "I" : 8}
    validacao = True

    # inserir jogada no formato correto 'A, 1: 1'
    jogada = input()

    if jogada[0].isalpha() and jogada[0] in letras:
        coluna = jogada[0]
    else:
        print("Coluna invalida")
        validacao = False

    if jogada[1] != ',' or jogada[3] != ':':
        print("Formato incorreto de jogada")
        validacao = False

    if jogada[2].isdigit():
        if int(jogada[2]) >= 0 and int(jogada[2]) <= 8:
            linha = int(jogada[2])
        else:
            print("Linha invalida")
            validacao = False
    else:
        print("Linha invalida")
        validacao = False

    if jogada[4].isdigit():
        if int(jogada[4]) > 0 and int(jogada[4]) < 10:
            numero = int(jogada[4])
        else:
            print("Numero invalido")
            validacao = False
    else:
        print("Numero invalido")
        validacao = False

    if validacao == True:
        print("Coluna: {}".format(coluna))
        print("Linha: {}".format(linha))
        print("Numero: {}".format(numero))
