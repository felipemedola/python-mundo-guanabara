preco = float(input('Qual é o preço do produto? R$'))
desconto = 5

novo_preco = preco * (1 - desconto / 100)

print('O produto que custava R${}, na promoção com desconto de {}% vai custar R${:.2f}.'.format(preco, desconto, novo_preco))