from random import randint
import time

itens = ('Pedra', 'Papel', 'Tesoura')
print('''Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opcao = int(input('Qual é a sua jogada? '))
opcao_pc = randint(0, 2)


print('JO')
time.sleep(0.8)
print('KEN')
time.sleep(0.8)
print('PO!!!')

print('-=' * 12)
print(f'Computador jogou {itens[opcao_pc]}')
print(f'Jogador jogou {itens[opcao]}')
print('-=' * 12)

if opcao == 0 and opcao_pc == 0 or opcao == 1 and opcao_pc == 1 or opcao == 2 and opcao_pc == 2:
      print('O jogo ficou empatado.')
elif opcao == 1 and opcao_pc == 0 or opcao == 2 and opcao_pc == 1:
      print('JOGADOR VENCE')
else:
      print('COMPUTADOR VENCE')