print('========== LOJAS GUANABARA ==========')
valor = float(input('Preço da compra: R$'))
print('FORMAS DE PAGAMENTO'
      '\n [ 1 ] à vista dinheiro/cheque'
      '\n [ 2 ] à vista cartão'
      '\n [ 3 ] 2x no cartão'
      '\n [ 4 ] 3x ou mais no cartão')
forma_pagamento = int(input('Qual é a opção? '))
desconto = 0
juros = 0
valor_final = 0

if forma_pagamento == 1:
    desconto = valor * 10 / 100
    valor_final = valor - desconto
elif forma_pagamento == 2:
    desconto = valor * 5 / 100
    valor_final = valor - desconto
elif forma_pagamento == 3:
    valor = valor_final
    valor_parcela = valor_final / 2
    print(f'Sua compra será parcelada em 2x de R${valor_parcela:.2f}')
elif forma_pagamento == 4:
    juros = valor * 20 / 100
    valor_final = valor + juros
    qtd_parcela = int(input('Quantas parcelas? '))
    valor_parcela = valor_final / qtd_parcela
    print(f'Sua compra será parcelada em {qtd_parcela}x de R${valor_parcela:.2f} COM JUROS')
else:
    valor = valor_final

print(f'Sua compra de R${valor:.2f} vai custar R${valor_final:.2f} no final.')