from validate_docbr import CPF

class Cpf:
    #Metodo construtor
    def __init__(self, cpf):
        cpf = str(cpf)
        if self.__cpf_eh_valido(cpf):
            self.__cpf = cpf
        else:
            raise ValueError("Cpf Inválido!!")
    #Fim do metodo __init__

    #Verifica se o cpf eh valido
    def __cpf_eh_valido(self, cpf):
        validador = CPF()
        return validador.validate(cpf)
    #Fim do metodo __cpf_eh_valido

    #Metodo get do cpf
    @property
    def cpf(self):
        return self.__cpf
    #Fim do metodo cpf

    #Formata o cpf para que ele fique com pontos e um traco
    def formatar_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    #Fim do metodo formatar_cpf

    #Metodo que converte a classe em str
    def __str__(self):
        return self.formatar_cpf()
    #Fim do metodo __str__