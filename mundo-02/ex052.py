numero = int(input('Digite um número: '))
primo = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        primo += 1
        print('\033[31m', f'{c}', end=' ')
    else:
        print('\033[33m', f'{c}', end=' ')

print('\033[m', f'\nO número {numero} foi divisível {primo} vezes')

if primo > 2:
    print('E por isso ele NÃO É PRIMO!')
else:
    print('E por isso ele É PRIMO!')