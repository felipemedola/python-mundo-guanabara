print('-=' * 9)
print('Tabuada dos Crias')
print('-=' * 9)

num = int(input('Digite um número: '))

for tab in range (1, 11):
    total = num * tab
    print(f'{num} * {tab:2} = {total}')
