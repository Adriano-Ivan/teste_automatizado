from unittest import TestCase

from src.leilao.dominio import Leilao, Usuario, Lance, Avaliador


class TestAvaliador(TestCase):
    def test_avalia(self):
        michael = Usuario('Michael')
        max = Usuario('Max')

        lance_do_max = Lance(max, 99.23)
        lance_do_michael = Lance(michael, 140.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_michael)
        leilao.lances.append(lance_do_max)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 99.23
        maior_valor_esperado = 140.00

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

