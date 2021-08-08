import sys
from copy import deepcopy

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if(valor <= self.__carteira):
            lance = Lance(self, valor)
            leilao.propoe(lance)
            self.__carteira -= valor
        else:
            print('Proposta recusada.')

    @property
    def carteira(self):
        return self.__carteira

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    def propoe(self, lance: Lance):
        if (not self.__lances or self.__lances[-1].usuario != lance.usuario and lance.valor > self.__lances[-1].valor):
            if (lance.valor > self.maior_lance):
                self.maior_lance = lance.valor
            if (lance.valor < self.menor_lance):
                self.menor_lance = lance.valor

            self.__lances.append(lance)
            return True

        if(lance.valor <= self.__lances[-1].valor):
            raise ValueError('O valor é inválido ! É preciso informar um valor maior que o do lance anterior !')

        if(self.__lances[-1].usuario == lance.usuario):
            raise ValueError('O usuário já fez um lance ! Não é permitido executar dois lances seguidos !')

    @property
    def lances(self):
        return deepcopy(self.__lances)


# class Avaliador:
#
#     def __init__(self):
#         self.maior_lance = sys.float_info.min
#         self.menor_lance = sys.float_info.max
#
#     def avalia(self, leilao: Leilao):
#
#         for lance in leilao.lances:
#             if(lance.valor > self.maior_lance):
#                 self.maior_lance = lance.valor
#             if(lance.valor < self.menor_lance):
#                 self.menor_lance = lance.valor