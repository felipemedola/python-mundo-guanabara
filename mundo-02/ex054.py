from datetime import date

ano_atual = date.today().year
menoridade = 0
maioridade = 0

for i in range(1, 8):
    ano_nascimento = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1

print(f'Ao todo tivemos {maioridade} pessoas maiores de idade')
print(f'E também tivemos {menoridade} pessoas menores de idade')