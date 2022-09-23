from validate_docbr import CNPJ

class Cnpj:
    #Metodo construtor
    def __init__(self, cnpj):
        cnpj = str(cnpj)
        if(self.__cnpj_eh_valido(cnpj)):
            self.__cnpj = cnpj
        else:
            raise ValueError("O CNPJ é inválido!!")
    #Fim do metodo __init__

    #Verifica se o cnpj eh valido
    def __cnpj_eh_valido(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)
    #Fim do metodo __cnpj_eh_valido

    #Metodo get do cnpj
    @property
    def cnpj(self):
        return self.__cnpj
    #Fim do metodo cnpj

    #Formata o cnpj para que ele fique com pontos e tracos
    def formatar_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
    #Fim do metodo formatar_cnpj

    #Metodo que converte a classe em str
    def __str__(self):
        return self.formatar_cnpj()
    #Fim do metodo __str__