from datetime import date

ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
alistamento = ano_nascimento + 18

print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')

if idade < 18:
    print(f'Ainda faltam {alistamento - ano_atual} anos para o alistamento.')
    print(f'Seu alistamento será em {alistamento}.')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {ano_atual - alistamento} anos.')
    print(f'Seu alistamento foi em {alistamento}.')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')