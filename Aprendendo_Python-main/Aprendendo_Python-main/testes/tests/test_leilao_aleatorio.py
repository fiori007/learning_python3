from unittest import TestCase
from src.leilao.usuario import Usuario
from src.leilao.lance import Lance
from src.leilao.leilao import Leilao
from src.leilao.excecoes import LanceInvalido
import random
import string

#Esta classe serve para relizar os testes nos metodos da classe Leilao
class TestLeilaoAleatorio(TestCase):
    #Este metodo serve para criar varios instancias da classe Usuario, cada um com um nome aleatorio
    #quantidade Numero de usuarios que serao gerados
    def cria_usuario(self, quantidade:int):
        self.usuarios = []
        for _ in range(quantidade):
            self.usuarios.append(Usuario(nome=''.join(random.choice(string.ascii_letters) for _ in range(2*quantidade)), carteira=500.0))
    #Fim do metodo cria_usuario

    #Este metodo serve para criar aleatoriamente valores para os lances
    #quantidade Quantidade de valores de lances que serao gerados
    def cria_valores_lances(self, quantidade:int):
        self.valor_lances = []
        for _ in range(quantidade):
            while(True):
                lance = random.randrange(0, 2 * quantidade)
                if (not lance in self.valor_lances):
                    self.valor_lances.append(lance)
                    break
    #Fim do metodo cria_valores_lances

    #Este metodo serve para criar os lances aleatoriamente
    #quantidade Quantidade de lances que serao criados e adicionados ao leilao
    #ordenar Valor booleano caso deseja ordenar os lances
    #inverter Valor booleano caso deseja ordenar com inversao
    def cria_lances_e_adiciona_ao_leilao(self, quantidade: int, ordenar=False, inverter=False):
        self.cria_usuario(quantidade)
        self.cria_valores_lances(quantidade)

        if ordenar:
            self.valor_lances.sort(reverse=inverter)

        # Criando os lances e adicionando ao leilao
        indice = 0
        while indice < quantidade:
            valor_lance = self.valor_lances[indice]
            usuario = self.usuarios[indice]
            lance = Lance(usuario, valor_lance)
            self.leilao.propoe(lance)
            indice += 1
    #Fim do metodo cria_lances_e_adiciona_ao_leilao

    # Este metodo serve para testar a classe Leilao passando a ela x lances aleatorios em ordem crescente e verificando o maior e o menor valor dos lances.
    # quantidade_de_lances Quantidade de lances aleatorios que serao inseridos no leilao.
    def test_quando_passado_x_lances_aleatorios_em_ordem_crescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance(self, quantidade_de_lances=999):
        #Criando os lances
        self.cria_lances_e_adiciona_ao_leilao(quantidade=quantidade_de_lances, ordenar=True)

        # Calculando o menor e o maior valor esperado
        menor_valor_esperado = min(self.valor_lances)
        maior_valor_esperado = max(self.valor_lances)

        # Comparando o menor e maior valor esperado com os valores obtidos
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    #Fim do metodo test_quando_passado_x_lances_aleatorios_em_ordem_crescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance

    # Este metodo serve para testar a classe Leilao passando a ela x lances aleatorios em ordem decrescente e verificando o maior e o menor valor dos lances.
    # quantidade_de_lances Quantidade de lances aleatorios que serao inseridos no leilao.
    def test_quando_passado_x_lances_aleatorios_em_ordem_decrescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance(self, quantidade_de_lances=999):
        #Criando os lances
        with(self.assertRaises(LanceInvalido)):
            self.cria_lances_e_adiciona_ao_leilao(quantidade=quantidade_de_lances, ordenar=True, inverter=True)

    #Fim do metodo test_quando_passado_x_lances_aleatorios_em_ordem_decrescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance

    #Este metodo serve para configurar o ambiente de teste
    def setUp(self):
        #Criando um leilao
        self.leilao = Leilao("Celular")
    #Fim do metodo setUp
#Fim da classe TestAvaliador