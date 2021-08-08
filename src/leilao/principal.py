from src.leilao.dominio import Usuario, Lance, Leilao

max = Usuario('Max')
michael = Usuario('Michael')

lance_do_michael = Lance(michael, 140.0)
lance_do_max = Lance(max, 99.23)

leilao = Leilao('Celular')

leilao.propoe(lance_do_max)
leilao.propoe(lance_do_michael)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')

print(f'O menor lance foi de {leilao.menor_lance} e o maior lance foi {leilao.maior_lance}')