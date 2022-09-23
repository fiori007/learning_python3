from unittest import TestCase
from src.leilao.usuario import Usuario
from src.leilao.lance import Lance
from src.leilao.leilao import Leilao
from src.leilao.excecoes import LanceInvalido

#Esta classe serve para relizar os testes nos metodos da classe Leilao
class TestLeilao(TestCase):
    #Este metodo serve para configurar o ambiente de teste
    def setUp(self):
        #Criando os usuarios Fulano, Ciclano e Ze
        self.fulano = Usuario("Fulano", 500.0)

        #Criando os lances de Fulano, Ciclano e Ze
        self.lance_do_fulano = Lance(self.fulano, 500)

        #Criando um leilao
        self.leilao = Leilao("Celular")
    #Fim do metodo setUp

    #Este metodo serve para testar a classe Avaliador passando a ela dois lances em ordem crescente e verificando o maior e o menor valor dos lances
    def test_quando_passado_dois_lances_em_ordem_crescente_deve_retornar_o_maior_e_menor_valor_de_um_lance(self):

        #Criando os usuarios ciclano
        ciclano = Usuario("Ciclano", 500.0)

        #Criando os lances do ciclano
        lance_do_ciclano = Lance(ciclano, 1500)

        #Adicionando os lances de Fulano e Ciclano ao leilao
        self.leilao.propoe(self.lance_do_fulano)
        self.leilao.propoe(lance_do_ciclano)

        #Definindo o menor e o maior valor esperado
        menor_valor_esperado = 500
        maior_valor_esperado = 1500

        #Comparando os valores
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    #Fim do metodo test_quando_passado_dois_lances_em_ordem_crescente_deve_retornar_o_maior_e_menor_valor_de_um_lance

    #Este metodo serve para verificar se a classe leilao vai permitir passar a ela dois lances em ordem decrescente
    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        #Verificando se a excecao, que deveria ocorrer, ocorre
        with(self.assertRaises(LanceInvalido)):
            #Criando os usuarios ciclano
            ciclano = Usuario("Ciclano", 500.0)

            #Criando os lances do ciclano
            lance_do_ciclano = Lance(ciclano, 1500)

            #Adicionando os lances de Fulano e Ciclano ao leilao
            self.leilao.propoe(lance_do_ciclano)
            self.leilao.propoe(self.lance_do_fulano)

    #Fim do metodo test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente

    #Este metodo serve para testar a classe Avaliador passando a ela apenas um lance e verificando o maior e o menor valor do lance
    def test_quando_passado_apenas_um_lance_no_leilao_deve_retornar_o_mesmo_valor_para_o_maior_e_o_menor_valor_de_um_lance(self):

        #Adicionando o lances do Ze
        self.leilao.propoe(self.lance_do_fulano)

        #Definindo o menor e o maior valor esperado
        valor_esperado = 500

        #Comparando os valores
        self.assertEqual(valor_esperado, self.leilao.menor_lance)
        self.assertEqual(valor_esperado, self.leilao.maior_lance)
    #Fim do metodo test_quando_passado_apenas_um_lance_no_leilao_deve_retornar_o_mesmo_valor_para_o_maior_e_o_menor_valor_de_um_lance

    #Este metodo serve para testar a classe leilao passando a ela tres lances e verificando o maior e o menor valor dos lances
    def test_quando_passado_tres_lances_deve_retornar_o_maior_e_menor_lance(self):
        #Criando os usuarios ciclano e ze
        ciclano = Usuario("Ciclano", 500.0)
        ze = Usuario("Zé", 500.0)

        #Criando os lances do ciclano e do ze
        lance_do_ciclano = Lance(ciclano, 1500)
        lance_do_ze = Lance(ze, 1200)

        #Adicionando os lances de Fulano e Ciclano ao leilao
        self.leilao.propoe(self.lance_do_fulano)
        self.leilao.propoe(lance_do_ze)
        self.leilao.propoe(lance_do_ciclano)

        #Definindo o menor e o maior valor esperado
        menor_valor_esperado = 500
        maior_valor_esperado = 1500

        #Comparando os valores
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    #Fim do metodo test_quando_passado_tres_lances_deve_retornar_o_maior_e_menor_lance

    #Este metodo serve para testar o caso de uso: Caso o leilao nao tiver lances deve permitir um usuario propor um lance
    def test_caso_o_leilao_nao_tiver_lance_deve_permitir_propor_um_lance(self):
        #Adicionando o lance do fulano
        self.leilao.propoe(self.lance_do_fulano)

        #Calculando a quantidade de lances
        quantidade_de_lances_recebido = len(self.leilao.lances)

        #Comparando os valores
        self.assertEqual(1, quantidade_de_lances_recebido)
    #Fim do metodo test_quando_leilao_nao_tiver_lance_deve_permitir_propor_um_lance

    #Este metodo serve para testar o caso de uso: Caso o ultimo usuario seja diferente deve permitir propor um lance
    def test_caso_o_ultimo_usuario_seja_diferente_deve_permitir_propor_um_lance(self):
        #Criando o usuario ze e o lance dele
        ze = Usuario("Zé", 500.0)
        lance_do_ze = Lance(ze, 200)

        #Adicionando o lance do fulano e do ze
        self.leilao.propoe(lance_do_ze)
        self.leilao.propoe(self.lance_do_fulano)

        #Calculando a quantidade de lances
        quantidade_de_lances = len(self.leilao.lances)

        #Comparando os valores
        self.assertEqual(2, quantidade_de_lances)
    #Fim do metodo test_caso_o_ultimo_usuario_seja_diferente_deve_permitir_propor_um_lance

    #Este metodo serve para testar o caso de uso: caso o usuario seja o mesmo nao deve permitir propor lance
    def test_caso_o_usuario_seja_o_mesmo_nao_deve_permitir_propor_lance(self):
        #Criando um outro lance para o usuario fulano
        lance_do_fulano_2000 = Lance(self.fulano, 2000)

        #Verificando se a excecao (que deveria ocorrer) ocorre
        with self.assertRaises(LanceInvalido):
        #Adicionando os lances do fulano
            self.leilao.propoe(self.lance_do_fulano)
            self.leilao.propoe(lance_do_fulano_2000)

    #Fim do metodo test_caso_o_usuario_seja_o_mesmo_nao_deve_permitir_propor_lance

#Fim da classe TestAvaliador
