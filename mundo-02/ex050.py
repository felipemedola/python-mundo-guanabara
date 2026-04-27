total = 0
cont = 0

for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        total += num
    cont += 1

print(f'Você informou {cont} números PARES e a soma foi {total}.')