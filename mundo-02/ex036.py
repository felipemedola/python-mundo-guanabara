valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do salário: R$'))
qtd_anos = int(input('Em quantos anos vai pagar? '))
qtd_parcela_mensal = qtd_anos * 12
valor_parcela_mensal = valor_casa / qtd_parcela_mensal
salario_percentual = salario * 0.3

print(f'Para pagar uma casa de R${valor_casa:.2f} em {qtd_anos} anos a prestação será de R${valor_parcela_mensal:.2f}.')

if valor_parcela_mensal > salario_percentual:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
