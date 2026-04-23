a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

menor = a
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

print('O maior valor é: {}'.format(maior))
print('O menor valor é: {}'.format(menor))