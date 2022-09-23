import forca
import adivinhacao

def escolher_jogo():
    #Exibindo a tela de bem vindo
    print("*********************************")
    print("********Escolha o seu jogo!******")
    print("*********************************")

    print("(1) Forca")
    print("(2) Adivinhacao")

    jogo=int(input("Qual jogo? "))

    if(jogo == 1):
        forca.jogar()
    elif(jogo == 2):
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolher_jogo()