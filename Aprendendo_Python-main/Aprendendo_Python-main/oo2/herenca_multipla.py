class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print("Horas registradas.")

    def mostra_tarefas(self):
        print("Faz muit coisa...")

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print("Faz muita coisa, Caelumer")

    def busca_curso_do_mes(self, mes=None):
        if(mes):
            print("Mostrando cursos - {}".format(mes))
        else:
            print("Mostrando cursos deste mês")

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print("Faz muita coisa, Alurete!")

    def buscar_perguntas_sem_respostas(self):
        print("Mostrando perguntas não respondidas no fórum")

class Hipster():
    def __str__(self):
        return "Hipster, {}".format(self.nome)

class Junior(Alura):
    pass

class Pleno(Alura, Caelum, Hipster):
    pass

joao = Junior("João da Silva")
joao.buscar_perguntas_sem_respostas()

pedro = Pleno("Pedro da silva")
pedro.buscar_perguntas_sem_respostas()
pedro.busca_curso_do_mes()
pedro.mostra_tarefas()
print(pedro)