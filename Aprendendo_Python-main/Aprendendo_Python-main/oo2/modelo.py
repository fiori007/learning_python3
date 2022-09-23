class Programa:
    #Metodo construtor
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    #Permite obter o valor de nome fora da classe
    @property
    def nome(self):
        return self._nome

    #Permite alterar o valor de nome fora da classe
    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    #Permite obter o valor de likes fora da classe
    @property
    def likes(self):
        return self._likes

    #Incrementa mais um do valor de likes
    def dar_like(self):
        self._likes += 1

    #Converte as informacoes da classe para String
    def __str__(self):
        return "Nome: {} - Ano: {} - Likes: {} .".format(self._nome, self.ano, self._likes)

class Filme(Programa):
    #Metodo construtor
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    #Converte as informacoes da classe para String
    def __str__(self):
        return "Nome: {} - Ano: {} - Duração: {} min - Likes: {} .".format(self._nome, self.ano, self.duracao, self._likes)

class Serie(Programa):
    #Metodo construtor
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    #Converte as informacoes da classe para String
    def __str__(self):
        return "Nome: {} - Ano: {} - Temporadas: {} - Likes: {} .".format(self._nome, self.ano, self.temporadas, self._likes)

class Playlist:
    #Metodo construtor
    def __init__(self, nome, programas):
        self.nome = nome
        self.__programas = programas

    #Retorna o tamanho
    def __len__(self):
        return len(self.__programas)

    #Torna a classe iteravel
    def __getitem__(self, item):
        return self.__programas[item]

