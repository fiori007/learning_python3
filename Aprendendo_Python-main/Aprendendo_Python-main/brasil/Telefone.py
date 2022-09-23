import re

class Telefone:
    #Este metodo serve para contruir uma instancia da classe
    #numero_telefone Numero de telefone que sera adicionado a classe
    def __init__(self, numero_telefone):
        #Convertendo numero_telefone para str caso ele esteja em outro formato
        numero_telefone = str(numero_telefone)

        #Verificando se o numero de telefone eh valido
        if(self.__telefone_eh_valido(numero_telefone)):
            self.__ddi, self.__ddd, self.__numero = self.__separar_numeros(numero_telefone)
        else:
            raise ValueError("O numero de telefone não é valido!!")
    #Fim do metodo __init__

    #Este metodo serve para verificar se um numero de telefone eh valido
    #numero_telefone Numero de telefone que sera verificado
    def __telefone_eh_valido(self, numero_telefone):
        padrao = "(\d{2,3})?[ ]?[(]?(\d{2})[)]?[ ]?(\d{4,5})[-]?(\d{4})"
        return bool(re.findall(padrao, numero_telefone))
    #Fim do metodo __telefone_eh_valido

    #Este metodo serve para formatar o numero de telefone
    def __formatar_numero(self):
        padrao = "(\d{4,5})[-]?(\d{4})"
        elementos_numero = re.search(padrao, self.__numero)
        return "+{}({}){}-{}".format(self.__ddi, self.__ddd, elementos_numero.group(1), elementos_numero.group(2))
    #Fim do metodo __formatar_numero

    #Este metodo serve para separar um numero de telefone completo em codigos ddi, ddd e o numero de telefone
    #numero_telefone_completo Numero de telefone contendo o ddi e o ddd
    def __separar_numeros(self, numero_telefone_completo):
        padrao = "(\d{2,3})?[ ]?[(]?(\d{2})[)]?[ ]?(\d{4,5})[-]?(\d{4})"
        elementos = re.search(padrao, numero_telefone_completo)
        ddi = elementos.group(1)
        ddd = elementos.group(2)
        numero = elementos.group(3)+elementos.group(4)

        if ddi is None:
            ddi = "55"

        return ddi, ddd, numero
    #Fim do metodo __separar_numeros

    #Este metodo serve para transformar uma instancia desta classe em uma str
    def __str__(self):
        return self.__formatar_numero()
    #Fim do metodo __str__