#Esta classe representa o lance que o usuario vai fazer no leilao
class Lance:
    #Este metodo serve para construir uma instancia da classe Lance
    #usuario Instancia da classe Usuario
    #valor Valor do lance
    def __init__(self, usuario, valor:float):
        self.usuario = usuario
        self.valor = float(valor)
    #Fim do metodo __init__
#Fim da classe Lance