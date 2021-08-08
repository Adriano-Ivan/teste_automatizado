from src.leilao.dominio import Usuario, Leilao
import pytest

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_esse_propor_um_lance():
    halgard = Usuario('Halgard', 100.00)

    leilao = Leilao('Celular')

    halgard.propoe_lance(leilao, 50.00)

    assert halgard.carteira == 50

def test_deve_permitir_propor_lance_quando_o_valor_e_menor_que_o_valor_da_carteira():
    sancho_panca = Usuario('Sancho Pança', 200.00)

    leilao = Leilao('Carreta')

    sancho_panca.propoe_lance(leilao, 10)

    assert sancho_panca.carteira == 190.00

def test_deve_permitir_propor_lance_quando_o_valor_e_igual_ao_valor_da_carteira():
    rodolfus = Usuario('Rodolfus', 500)

    leilao = Leilao('Espada')

    rodolfus.propoe_lance(leilao, 500)

    assert rodolfus.carteira == 0

def test_nao_deve_permitir_propor_lance_quando_o_valor_for_maior_que_o_valor_da_carteir():
    maxilis = Usuario('Maxilis', 500)

    leilao = Leilao('Lança')

    maxilis.propoe_lance(leilao, 600)

    assert maxilis.carteira == 500