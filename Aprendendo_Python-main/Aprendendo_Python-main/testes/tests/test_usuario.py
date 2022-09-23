from src.leilao.usuario import Usuario
from src.leilao.leilao import Leilao
from src.leilao.excecoes import LanceInvalido

import pytest

#Esta funcao serve para passar para cada funcao uma instancia da classe Usuario
@pytest.fixture()
def ze():
    return Usuario(nome="Zé", carteira=500.0)
#Fim do metodo ze

#Esta funcao serve para passar para cada funcao uma instancia da classe Leilao
@pytest.fixture()
def leilao():
    return Leilao("Chinelo")
#Fim do metodo leilao

#Esta funcao serve para testar o caso de uso que quando um lance eh proposto isso deve subtrair o valor da carteira do usuario
def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(ze, leilao):

    #Proponro o lance do joao
    ze.propoe_lance(leilao, 250.0)

    #Verificando o valor da carteira do Joao
    assert ze.carteira == 250.0
#Fim do metodo test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance

#Esta funcao serve para testar o caso de uso que deve permitir a um usuario propor um lance menor que o valor da carteira dele
def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(ze, leilao):

    #Adicionando o lance
    ze.propoe_lance(leilao, 1.0)

    #Verificando o valor da carteira
    assert ze.carteira == 499
#Fim do metodo test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira

#Esta funcao serve para testar o caso de uso que deve permitir a um usuario propor um lance com um valor igual ao de sua carteira
def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(ze, leilao):

    # Adicionando o lance
    ze.propoe_lance(leilao, 500.0)

    # Verificando o valor da carteira
    assert ze.carteira == 0
#Fim do metodo test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira

#Esta funcao serve para testar o caso de uso que nao deve permitir a um usuario propor um lance maior que o valor de sua carteira
def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(ze, leilao):

    #Verificando se a excecao, que deveria ocorrer, ocorre
    with pytest.raises(LanceInvalido):

        # Adicionando o lance
        ze.propoe_lance(leilao, 600.0)
#Fim do metodo test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira