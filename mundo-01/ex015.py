dias_alugado = int(input('Quantos dias alugado: '))
dist_percorrida = float(input('Quantos Km rodado: '))

custo_carro = 60
custo_distancia = 0.15
valor_aluguel = (dias_alugado * custo_carro) + (dist_percorrida *  custo_distancia)

print('O total a pagar é de R${:.2f}'.format(valor_aluguel))