velocidade_carro = int(input('Qual é a velocidade atual do carro? '))
velocidade_permitida = 80

if velocidade_carro > velocidade_permitida:
    print('MULTADO! Você excedeu o limite permitido que é {}Km/h'.format(velocidade_permitida))
    multa = (velocidade_carro - velocidade_permitida) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')