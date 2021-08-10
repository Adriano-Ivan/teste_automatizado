import sys
from copy import deepcopy
from src.leilao.excecoes import LanceInvalido

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def __lance_e_valido(self, valor):
        return valor <= self.__carteira

    def propoe_lance(self, leilao, valor):
        if(self.__lance_e_valido(valor)):
            lance = Lance(self, valor)
            leilao.propoe(lance)
            self.__carteira -= valor
        else:
            raise LanceInvalido('O lance proposto tem um valor maior que o da carteira !')

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
        self.maior_lance = 0
        self.menor_lance = 0
        # self.maior_lance = sys.float_info.min
        # self.menor_lance = sys.float_info.max

    def __tem_lances(self):
        return self.__lances

    def __sao_usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido('O mesmo usuário não pode dar dois lances seguidos !')

    def __valor_e_maior_que_o_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido('O valor do lance deve ser maior que o do lance anterior !')

    def __lance_e_valido(self, lance):
        return (not self.__tem_lances() or self.__sao_usuarios_diferentes(lance) and
                self.__valor_e_maior_que_o_anterior(lance))

    def propoe(self, lance: Lance):
        if self.__lance_e_valido(lance):
            if not self.__tem_lances():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise LanceInvalido('O usuário já fez um lance ! Não é permitido executar dois lances seguidos !')
        # if(lance.valor <= self.__lances[-1].valor):
        #     raise ValueError('O valor é inválido ! É preciso informar um valor maior que o do lance anterior !')

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