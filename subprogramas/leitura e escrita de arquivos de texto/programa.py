print("Digite uma opcao:\n1 - Escrever no arquivo de texto.\n2 - Adicionar texto ao arquivo existente.\n3 - Ler o arquivo de texto.")
selecao = int(input())

if selecao == 1:
    print("Digite o texto que voce deseja salvar no arquivo:")
    texto = input()
    arquivo = open("arquivo de texto.txt", "w")
    arquivo.write(texto)
    arquivo.close()
    print("Arquivo salvo!")

elif selecao == 2:
    print("Digite o texto que voce deseja adicionar ao arquivo:")
    texto = input()
    arquivo = open("arquivo de texto.txt", "a")
    arquivo.write("\n" + texto)
    arquivo.close()
    print("Arquivo salvo!")

elif selecao == 3:
    arquivo = open("arquivo de texto.txt", "r")
    texto = arquivo.read()
    print(texto)
    arquivo.close()