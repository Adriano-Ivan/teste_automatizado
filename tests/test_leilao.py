from unittest import TestCase

from src.leilao.dominio import Leilao, Usuario, Lance
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.michael = Usuario('Michael', 500)
        self.max = Usuario('Max', 500)

        self.lance_do_max = Lance(self.max, 99.23)
        self.lance_do_michael = Lance(self.michael, 140.0)

        self.leilao = Leilao('Celular')

    def test_nao_deve_permitir_propor_um_lance_quando_valores_forem_adicionados_de_forma_decrescente(self):

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_michael)
            self.leilao.propoe(self.lance_do_max)

            # self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
            # self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

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
        maxwell = Usuario('Maxwell', 500)

        lance_do_maxwell = Lance(maxwell, 210.23)

        self.leilao.propoe(self.lance_do_max)
        self.leilao.propoe(self.lance_do_michael)
        self.leilao.propoe(lance_do_maxwell)

        menor_valor_esperado = 99.23
        maior_valor_esperado = 210.23

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # Se o leil??o n??o tiver lances, deve permitir propor um lance
    def teste_deve_permitir_propor_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_max)

        quantidade_de_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebidos)

    # Se o ??ltimo usu??rio for diferente, deve permitir propor um lance
    def teste_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuris = Usuario('Yuris',500)

        lance_do_yuris = Lance(yuris, 233)

        self.leilao.propoe(self.lance_do_michael)
        self.leilao.propoe(lance_do_yuris)

        quantidade_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebidos)

    # Se o ??ltimo usu??rio for o mesmo, ele n??o deve permitir propor um lance
    def teste_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_michael140 = Lance(self.michael, 140.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_michael)
            self.leilao.propoe(lance_do_michael140)

            # quantidade_de_lances_recebidos = len(self.leilao.lances)
            # self.assertEquals(1, quantidade_de_lances_recebidos)


