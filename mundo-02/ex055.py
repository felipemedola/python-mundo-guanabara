maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))

    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi de {maior:.1f}Kg')
print(f'O menor peso lido foi de {menor:.1f}Kg')
