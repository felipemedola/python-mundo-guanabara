primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = ((primeiro + 1) * razao) * 10

for c in range(primeiro, decimo, razao):
    print(f'{c}', end=' > ')
print('ACABOU!')