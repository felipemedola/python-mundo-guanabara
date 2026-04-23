distancia = int(input('Qual é a distância da viagem? '))
distancia_promocional = 200
print('Você está prestes a começar uma viagem de {:.1f}KM.'.format(distancia))
total = distancia * 0.5 if distancia <= distancia_promocional else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(total))

