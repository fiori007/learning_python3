from Cnpj import Cnpj
from Cpf import Cpf

class Documento:

    #Este metodo cria um objeto documento (cpf, cnpj) de acordo com o tamanho da string passada
    @staticmethod
    def criar_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            objeto_documento = Cpf(documento)
        elif len(documento) == 14:
            objeto_documento = Cnpj(documento)
        else:
            raise ValueError("Valor inválido!!")

        return objeto_documento
    #Fim do metodo criar_documento