from src.leilao.dominio import Usuario, Leilao
import pytest

@pytest.fixture
def halgard():
    return Usuario('Halgard', 100.00)

@pytest.fixture
def sancho_panca():
    return Usuario('Sancho Pança', 200.00)

@pytest.fixture
def rodolfus():
    return Usuario('Rodolfus', 500)

@pytest.fixture
def maxilis():
    return Usuario('Maxilis', 500)

@pytest.fixture
def leilao():
    return Leilao('Lança')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_esse_propor_um_lance(halgard, leilao):
    halgard.propoe_lance(leilao, 50.00)

    assert halgard.carteira == 50

def test_deve_permitir_propor_lance_quando_o_valor_e_menor_que_o_valor_da_carteira(sancho_panca, leilao):
    sancho_panca.propoe_lance(leilao, 10)

    assert sancho_panca.carteira == 190.00

def test_deve_permitir_propor_lance_quando_o_valor_e_igual_ao_valor_da_carteira(rodolfus, leilao):
    rodolfus.propoe_lance(leilao, 500)

    assert rodolfus.carteira == 0

def test_nao_deve_permitir_propor_lance_quando_o_valor_for_maior_que_o_valor_da_carteir(maxilis, leilao):
    with pytest.raises(ValueError):
        maxilis.propoe_lance(leilao, 600)

        # assert maxilis.carteira == 500