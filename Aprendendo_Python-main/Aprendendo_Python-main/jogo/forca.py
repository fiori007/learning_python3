import random

#Exibindo a tela de bem vindo
def imprimir_bem_vindo():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

#Obtem a palavra secreta de forma aleatoria do arquivo
def obter_palavra_secreta(nome_arquivo="palavras.txt", primeira_linha=0):
    # Lendo o arquivo de palavras
    with open(nome_arquivo, "r") as arquivo:
        palavras = []

        #Lendo linha por linha
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    #Escolhendo uma palavra aleatoriamente
    numero = random.randrange(primeira_linha, len(palavras))
    palavra_secreta=palavras[numero]

    return palavra_secreta

#Obtem da entrada padrao o chute do jogador, tratando a entrada
def obter_chute():
    # Obtendo o chute
    chute = input("Qual letra? ")

    # Tratando o chute do usuario, removendo os espacos e convertendo para mnusculo
    chute = chute.strip()
    chute = chute.lower()

    return chute

#Verifica se o chute contem na palavra secreta, e caso verdadeiro modifica as letras acertadas
def testa_e_adiciona_chute(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = chute
        index += 1

    return letras_acertadas

#Imprime mensagem de resultado
def imprime_resultado(acertou, palavra_secreta):
    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

#Imprime a mensagem de perdedor com o desenho feito pelo instrutor Nico Steppat da Alura Cursos Online
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

#Imprime a mensagem de vencedor com o desenho feito pelo instrutor Nico Steppat da Alura Cursos Online
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

#Imprime o desenho da forca feito pelo instrutor Nico Steppat da Alura Cursos Online
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    elif(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    elif(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    elif(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    elif(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    elif(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    elif(erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

#Roda o jogo
def jogar():

    imprimir_bem_vindo()

    palavra_secreta = obter_palavra_secreta()

    # Inicializando as letras acertadas
    letras_acertadas = ["_" for letra in palavra_secreta]

    letras_erradas = []
    maximo_tentativas = 7

    #Convertendo a palavra_secreta para lower
    palavra_secreta = palavra_secreta.lower()

    #Inicializando as variaveis de controle do laco
    enforcou=False
    acertou=False

    while((not enforcou) and (not acertou)):

        #Exibindo as letras acertadas e erradas
        print("Letras acertadas: {}.".format(letras_acertadas))
        print("Letras erradas: {}.".format(letras_erradas))

        #Obtendo o chute do jogador
        chute = obter_chute()

        #Verificando se a palavra digitada pelo usuario se encontra na pelavra secreta
        if(chute in palavra_secreta):
            letras_acertadas=testa_e_adiciona_chute(palavra_secreta, chute, letras_acertadas)

        else:
            letras_erradas.append(chute)
            letras_erradas.sort()
            print("Voce errou. Restam {} tentativas".format(maximo_tentativas-len(letras_erradas)))
            desenha_forca(len(letras_erradas))

        #Verificando se o usuario acertou ou se enforcou
        acertou =(not "_" in letras_acertadas)
        enforcou = (len(letras_erradas) >= maximo_tentativas)

    #Exibindo mensagem caso o usuario se enforque o ganhe o jogo
    imprime_resultado(acertou, palavra_secreta)

    #Exibindo mensagem de fim de jogo
    print("Fim do jogo")
    print("A palavra secreta eh: {}".format(palavra_secreta))

#Inicia a funcao jogar caso execute diretamente deste arquivo
if(__name__ == "__main__"):
    jogar()