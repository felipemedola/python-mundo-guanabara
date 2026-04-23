from datetime import date

ano_nascimento = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f'O atleta tem {idade} anos.')

if idade > 25:
    print('Classificação: MASTER')
elif 19 < idade <= 25:
    print('Classificação: SÊNIOR')
elif 14 < idade <= 19:
    print('Classificação: JUNIOR')
elif 9 < idade <= 14:
    print('Classificação: INFANTIL')
else:
    print('Classificação MIRIM')