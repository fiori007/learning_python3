#Importando a biblioteca do random
import random

def jogar():
    #Exibindo a tela de bem vindo
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhacao!")
    print("*********************************")

    #Obtendo o nivel de dificuldade
    print("Qual o nivel de dificuldade?")
    print("(1) Facil")
    print("(2) Medio")
    print("(3) Dificil")
    nivel=int(input("Nivel: "))

    #Configurando a quantidade de tentativas de acordo com o nivel de dificuldade
    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    elif(nivel == 3):
        total_tentativas = 5

    #Gerando o numero secreto
    numero_secreto = random.randrange(1, 101)

    pontos=1000

    #Rodando as rodadas
    for rodada in range(1, total_tentativas+1):

        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute = int(input("Digite o seu numero entre 1 e 100: "))
        print("Voce digitou ", chute)

        #Exibindo mensagem de erro caso usuario digite um numero invalido
        if(chute < 1 or chute > 100):
            print("O numero tem que ser entre 1 e 100!")
            continue

        #Configurando as variaveis booleanas
        acertou= (chute == numero_secreto)
        maior= (chute > numero_secreto)
        menor= (chute < numero_secreto)

        #Exibindo mensagens de acerto ou erro
        if(acertou):
            print("Voce acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("O numero digitado eh maior que o numero secreto")
            elif(menor):
                print("O numero digitado eh menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

            if(rodada == total_tentativas):
                print("O numero secreto era {}. Voce fez {} pontos.".format(numero_secreto, pontos))

    #Exibindo mensagem de fim de jogo
    print("Fim do jogo")
    print("O numero secreto foi {}.".format(numero_secreto))

if(__name__ == "__main__"):
    jogar()