class Cliente:
    #Metodo construtor
    def __init__(self, nome):
        self.__nome=nome

    #Permite acessar o valor da variavel nome fora da classe
    @property
    def nome(self):
        return self.__nome.title()

    #Permite alterar o valor da variavel nome fora da classe
    @nome.setter
    def nome(self, nome):
        self.__nome = nome