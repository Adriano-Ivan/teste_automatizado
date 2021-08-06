from unittest import TestCase

from src.leilao.dominio import Leilao, Usuario, Lance


class TestAvaliador(TestCase):

    def setUp(self):
        self.michael = Usuario('Michael')
        self.max = Usuario('Max')

        self.lance_do_max = Lance(self.max, 99.23)
        self.lance_do_michael = Lance(self.michael, 140.0)

        self.leilao = Leilao('Celular')

    def test_que_retorna_maior_e_menor_valor_quando_adicionados_de_forma_decrescente(self):
        self.leilao.propoe(self.lance_do_michael)
        self.leilao.propoe(self.lance_do_max)

        menor_valor_esperado = 99.23
        maior_valor_esperado = 140.00

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_que_retorna_maior_e_menor_valor_quando_adicionados_de_forma_crescente(self):
        self.leilao.propoe(self.lance_do_max)
        self.leilao.propoe(self.lance_do_michael)

        menor_valor_esperado = 99.23
        maior_valor_esperado = 140.00

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado,self.leilao.maior_lance)

    def test_que_deve_retornar_o_mesmo_valor_para_o_menor_e_o_maior_lance_quando_o_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_max)

        self.assertEqual(99.23, self.leilao.menor_lance)
        self.assertEqual(99.23, self.leilao.maior_lance)

    def test_que_deve_retornar_maior_e_menor_lance_quando_o_leilao_tiver_tres_lances(self):
        maxwell = Usuario('Maxwell')

        lance_do_maxwell = Lance(maxwell, 210.23)

        self.leilao.propoe(self.lance_do_max)
        self.leilao.propoe(self.lance_do_michael)
        self.leilao.propoe(lance_do_maxwell)

        menor_valor_esperado = 99.23
        maior_valor_esperado = 210.23

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
