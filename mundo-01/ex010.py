money = float(input('Quanto de dinheiro você tem? R$'))
dolar = 3.27
conv = money / dolar

print('Com R${:.2f} você pode comprar US${:.2f}'.format(money, conv))