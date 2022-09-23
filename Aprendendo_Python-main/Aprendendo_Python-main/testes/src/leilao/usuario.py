from src.leilao.excecoes import LanceInvalido
from src.leilao.lance import Lance
from src.leilao.leilao import Leilao

#Esta classe representa o usuario que vai fazer lances no leilao
class Usuario:
    #Este metodo serve para construir uma instancia da classe Usuario
    #nome Nome do usuario
    def __init__(self, nome: str, carteira:float):
        self.__nome = nome
        self.__carteira = carteira
    #Fim do metodo __init__

    #Este metodo serve para obter o nome de uma instancia da classe Usuario
    @property
    def nome(self):
        return self.__nome
    #Fim do metodo nome

    #Este metodo serve para obter o valor da carteira de uma instancia da classe Usuario
    @property
    def carteira(self):
        return self.__carteira
    #Fim do metodo carteira

    #Este metodo serve para uma instancia da classe Usuario poder propor um lance.
    #leilao Instancia da classe Leilao a qual o usuario ira propor um lance
    #valor Valor do lance proposto pelo usuario
    def propoe_lance(self, leilao:Leilao, valor:float):
        if not self.__valor_eh_valido(valor):
            raise LanceInvalido("O valor proposto eh maior que o valor da carteira.")
        lance = Lance(self, valor)
        leilao.propoe(lance)

        self.__carteira -= valor
    #Fim do metodo propoe_lance

    #Este metodo serve para verificar se o valor do leilao eh valido (menor ou igual ao valor da carteira do usuario)
    #valor Valor do lance que sera verificado se ele eh valido
    def __valor_eh_valido(self, valor:float):
        return valor <= self.__carteira
    #Fim do metodo __valor_eh_valido

#Fim da classe Usuario