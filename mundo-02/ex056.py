total_age = 0
total_women = 0
oldest_man_age = 0
oldest_man_name = ''

for i in range (1, 5):
    print(f'----- {i}ª PESSOA -----')
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    gender = str(input('Sexo [M/F]: ')).strip().upper()
    total_age += age
    if gender == 'M':
        if age > oldest_man_age:
            oldest_man_age = age
            oldest_man_name = name
    if gender == 'F':
        if age < 20:
            total_women += 1

average_age = total_age / i

print(f'A média de idade do grupo é de {average_age:.1f} anos.')
print(f'O homem mais velho tem {oldest_man_age} anos e se chama {oldest_man_name}.')
print(f'Ao todo são {total_women} mulheres com menos de 20 anos.')