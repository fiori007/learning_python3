class ExtratorArgumentosUrl:
    #Metodo construtor
    def __init__(self, url):
        self.url = url

    #Metodo que converte a classe em string
    def __str__(self):
        moeda_origem, moeda_destino = self.obter_nome_moedas()
        return ("URL: " + self.url + "\nParametros:\nValor: " + str(self.obter_valor()) + ".\nMoeda Origem: " + str(moeda_origem) + ".\nMoeda Destino: " + str(moeda_destino) + ".")

    #Metodo que obtem o tamanho da classe
    def __len__(self):
        return len(self.url)

    #Metodo que compara dois objetos desta mesma classe para ver se sao iguais
    def __eq__(self, other):
        return self.url == other.url

    #Metodo que compara dois objetos desta mesma classe para ver se sao diferentes
    def __ne__(self, other):
        return not self.__eq__(other)

    #Retorna o valor da variavel url
    @property
    def url(self):
        return self.__url

    #Altera o valor da variavel url
    @url.setter
    def url(self, url):
        if self.string_eh_valida(url):
            self.__url = url
        else:
            raise InvalidUrlException()

    def obter_valor(self):
        #Declarando o argumento de valor
        argumento_valor="valor"

        #Obtendo o valor
        indice_inicial_valor = self.__obter_indice_inicial_do_argumento(argumento_valor)
        indice_final_valor = self.url.find("%", indice_inicial_valor)
        valor = self.url[indice_inicial_valor:indice_final_valor]

        return valor



    #Retorna os nomes das moedas de origem e de destino respectivamente
    def obter_nome_moedas(self):
        #Declarando os argumentos utilizados na URL para definir as moedas de origem e destino
        argumento_moeda_origem = "moedaorigem"
        argumento_moeda_destino = "moedadestino"

        #Obtendo a moeda de origem
        indice_inicial_moeda_origem = self.__obter_indice_inicial_do_argumento(argumento_moeda_origem)
        indice_final_moeda_origem = self.url.find("&", indice_inicial_moeda_origem)
        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        #Obtendo a moeda de destino
        indice_inicial_moeda_destino = self.__obter_indice_inicial_do_argumento(argumento_moeda_destino)
        indice_final_moeda_destino = self.url.find("&", indice_inicial_moeda_destino)
        moeda_destino = self.url[indice_inicial_moeda_destino:indice_final_moeda_destino]

        if not (self.verificar_moeda(moeda_origem) and self.verificar_moeda(moeda_destino)):
            raise ClassConstructionException()

        return moeda_origem, moeda_destino

    #Retorna o indice inicial do argumento da URL
    def __obter_indice_inicial_do_argumento(self, parametro):
        return self.url.find(parametro) + len(parametro) + 1

    #Verifica se uma string eh valida
    @staticmethod
    def string_eh_valida(string):
        return (string is not None) and (type(string) == str) and bool(string)

    #Verifica se uma moeda eh valida
    @staticmethod
    def verificar_moeda(moeda):
        return not(moeda.lower() == "moedadestino" or moeda.lower() == "moedaorigem")

#Excecao que ocorre ao construir uma classe de forma errada
class ClassConstructionException(Exception):
    #Metodo construtor
    def __init__(self, message="THIS CLASS WAS BUILT WRONG"):
        self.message = message
        super().__init__(self.message)

#Excecao que ocorre ao inserir um URL invalido na construcao da classe ou na alteracao do url
class InvalidUrlException:
    # Metodo construtor
    def __init__(self, message="THIS URL IS INVALID"):
        self.message = message
        super().__init__(self.message)