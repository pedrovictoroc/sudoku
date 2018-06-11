vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
validacao = True
for i in range(0, len(vetor)):
    for j in range(i+1, len(vetor)):
        if vetor[i] == vetor[j]:
            validacao = False
            print("{} esta repetido".format(vetor[i]))
if validacao:
    print("Nenhum elemento repetido")
