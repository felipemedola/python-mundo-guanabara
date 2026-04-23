total = 0
count = 0

for num in range(1, 501):
    if num %2 == 1: #Se for impar...
        if num %3 == 0: #Se for divisível por 3...
            total += num #Então ele soma o numero ao total.
            count += 1

print(f'A soma de todos os {count} valores solicitados é {total}')