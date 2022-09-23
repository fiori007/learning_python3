class Conta:

    #Metodo construtor
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco="001"

    #Imprime o extrato da conta
    def extrato(self):
        print("Saldo de R${} do titular {}".format(self.__saldo, self.__titular))

    #Deposita um determinado valor na conta
    def depositar(self, valor):
        self.__saldo += valor

    #Verifica se eh possivel sacar determinado valor
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar=self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    #Saca um determinado valor da conta
    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    #Transfere dinheiro entre contas
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    #Permite acessar o valor da variavel saldo fora da classe
    @property
    def saldo(self):
        return self.__saldo

    #Permite acessar o valor da variavel titular fora da classe
    @property
    def titular(self):
        return self.__titular

    #Permite acessar o valor da variavel limite fora da classe
    @property
    def limite(self):
        return self.__limite

    #Permite acessar o valor da variavel numero fora da classe
    @property
    def numero(self):
        return self.__numero

    #Permite alterar o valor da variavel limite fora da classe
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    #Retorna o codigo deste banco
    @staticmethod
    def codigo_banco():
        return "001"

    #Retorna os codigos de todos os bancos
    @staticmethod
    def codigos_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}