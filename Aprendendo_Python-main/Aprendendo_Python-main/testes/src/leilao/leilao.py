from src.leilao.lance import Lance
from src.leilao.excecoes import LanceInvalido

#Esta classe serve para armazenar os lances do leilao
class Leilao:
    #Este metodo serve para construir uma instancia da classe Leilao
    #descricao Descricao do leilao
    def __init__(self, descricao:str):
        self.descricao = descricao
        self.__lances = []
    #Fim do metodo __init__

    #Este metodo serve para obter uma copia dos lances de uma instancia da classe Leilao
    @property
    def lances(self):
        return self.__lances[:]
    #Fim do metodo lances

    #Este metodo serve para adicionar um novo lance a instancia da classe Leilao
    #lance Instancia da classe Lance que sera adicionada ao leilao
    def propoe(self, lance:Lance):

        #Verificando se nao ha lances no leilao
        if not self.__tem_lances():
            #Salvando o menor lance
            self.__menor_lance = lance.valor

            #Salvando o maior lance
            self.__maior_lance = lance.valor

            #Adicionando o lance
            self.__lances.append(lance)

        #Verificando se o mesmo usuario nao fez dois lances seguidos e se o valor do lance eh maior que o valor do lance anterior
        elif(self.__usuarios_diferentes(lance)) and (self.__valor_maior_que_o_anterior(lance)):

            #Salvando o maior lance
            self.__maior_lance = lance.valor

            #Adicionando o lance
            self.__lances.append(lance)

        #Gerando excecao caso um mesmo usuario proponha dois lances seguidos
        elif (self.__lances[-1].usuario == lance.usuario):
            raise LanceInvalido("Um usuário não pode propor dois lances seguidos.")

        #Gerando excecao caso o valor de um lance seja inferior ao de um lance anterior
        elif (lance.valor <= self.__lances[-1].valor):
            raise LanceInvalido("O lance deve ser maior que o lance anterior.")
    #Fim do metodo propoe

    #Este metodo serve para indicar se a instancia da classe Leilao possui algum lance
    def __tem_lances(self):
        return bool(self.__lances)
    #Fim do metodo __tem_lances

    #Este metodo serve para verificar se o usuario de um lance eh diferente do usuario do lance anterior
    #lance Lance cujo usuario sera verificado com o usuario do lance anterior
    def __usuarios_diferentes(self, lance):
        return self.__lances[-1].usuario != lance.usuario
    #Fim do metodo __usuarios_diferentes

    #Este metodo serve para verificar se o valor do lance eh maior que o valor de um lance anterior
    #lance Lance cujo valor sera verificado com o do lance anterior
    def __valor_maior_que_o_anterior(self, lance):
        return lance.valor > self.__lances[-1].valor
    #Fim do metodo __valor_maior_que_o_anterior

    #Este metodo serve para obter o maior lance de uma instancia da classe Leilao
    @property
    def maior_lance(self):
        return self.__maior_lance
    #Fim do metodo maior_lance

    #Este metodo serve para obter o menor lance de uma instancia da classe Leilao
    @property
    def menor_lance(self):
        return self.__menor_lance
    #Fim do metodo menor_lance

#Fim da classe Leilao