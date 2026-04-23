import random
from time import sleep

computador = random.randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar

print('PROCESSANDO...')
sleep(2)

if jogador != computador:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
else:
    print('PARABÉNS! Você conseguiu me vencer!')