from datetime import datetime, timedelta

class DataHora:
    #Este metodo constroi uma instancia desta classe
    #data_e_hora Data e hora no formato datetime da data e hora que deseja armazenar nessa classe
    def __init__(self, data_e_hora=None):
        if data_e_hora is None:
            data_e_hora = datetime.now()
        self.data_e_hora = data_e_hora
    #Fim do metodo __init__

    #Este metodo serve para obter o nome do dia da semana da instancia desta classe.
    def dia_semana(self):
        dias_semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
        return dias_semana[self.data_e_hora.weekday()]
    #Fim do metodo dia_semana

    #Este metodo serve para obter o numero do mes da instancia desta classe
    def nome_do_mes(self):
        meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
        return meses[self.data_e_hora.month-1]
    #Fim do metodo nome_do_mes

    #Este metodo serve para converter uma instancia desta classe em uma str
    def __str__(self):
        return datetime.strftime(self.data_e_hora, "%d/%m/%Y %H:%M:%S")
    #Fim do metodo __str__

    #Este metodo serve para somar uma instancia desta classe com outra
    def __add__(self, other):
        return DataHora(self.data_e_hora + other.data_e_hora)
    #Fim do metodo __add__

    #Este metodo serve para subtrair uma instancia desta classe com outra
    def __sub__(self, other):
        return DataHora(self.data_e_hora - other.data_e_hora)
    #Fim do metodo __sub__

    #Este metodo serve para calcular a quantidade de data e hora que se passou da data e hora da instancia da classe a data e hora de hoje
    def tempo_passado(self):
        return datetime.now() - self.data_e_hora
    #Fim do metodo tempo_passado