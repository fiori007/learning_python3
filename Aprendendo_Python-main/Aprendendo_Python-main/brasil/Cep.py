import requests

class Cep:
    #Este metodo constroi uma instancia desta classe
    #cep Numero do cep que sera usado para construir a instancia da classe
    def __init__(self, cep):
        cep = str(cep)
        if self.__cep_eh_vlido(cep):
            self.__cep = cep
            self.__busca_cep()
        else:
            raise ValueError("O CEP é inválido!!")
    #Fim do metodo __init__

    #Este metodo serve para verificar se um cep eh valido
    #cep Numero de cep que sera verificado se eh valido
    def __cep_eh_vlido(self, cep):
        return len(cep) == 8
    #Fim do metodo __cep_eh_valido

    #Este metodo serve para formatar o numero do cep
    def __formatar_cep(self):
        return "{}-{}".format(self.__cep[:5], self.__cep[5:])
    #Fim do metodo __formatar_cep

    #Este metodo serve para converter uma instancia desta classe em uma str
    def __str__(self):
        #return self.__formatar_cep()
        return self.__formatar_cep() + " : " + self.__unidade_federativa + " , " + self.__localidade + " , " + self.__bairro + " , " + self.__logradouro + " , " +self.__complemento
    #Fim do metodo __str__

    #Este metodo serve para buscar informacoes sobre um determindo cep e atribuir essas informacoes a instancia desta classe
    def __busca_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.__cep)
        requisicao = requests.get(url)
        dados_obtidos = requisicao.json()

        self.__unidade_federativa = dados_obtidos["uf"]
        self.__localidade = dados_obtidos["localidade"]
        self.__bairro = dados_obtidos["bairro"]
        self.__logradouro = dados_obtidos["logradouro"]
        self.__complemento = dados_obtidos["complemento"]
    #Fim do metodo __busca_cep

    #Este metodo serve para obter a unidade federativa do cep
    @property
    def unidade_federativa(self):
        return self.__unidade_federativa
    #Fim do metodo unidade_federativa

    #Este metodo serve para obter a localidade do cep
    @property
    def localidade(self):
        return self.__localidade
    #Fim do metodo localidade

    #Este metodo serve para obter o bairro do cep
    @property
    def bairro(self):
        return self.__bairro
    #Fim do metodo bairro

    #Este metodo serve para obter o logradouro do cep
    @property
    def logradouro(self):
        return self.__logradouro
    #Fim do metodo logradouro

    #Este metodo serve para obter o complemento do cep
    @property
    def complemento(self):
        return self.__complemento
    #Fim do metodo complemento