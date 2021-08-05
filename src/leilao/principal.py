from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

max = Usuario('Max')
michael = Usuario('Michael')

lance_do_max = Lance(max, 99.23)
lance_do_michael = Lance(michael, 140.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_max)
leilao.lances.append(lance_do_michael)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi {avaliador.maior_lance}')