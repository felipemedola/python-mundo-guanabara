num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2:
    print(f'O PRIMEIRO número ({num1}) é maior que o segundo número ({num2}).')
elif num2 > num1:
    print(f'O SEGUNDO número ({num2}) é maior que o primeiro número ({num1}).')
else:
    print('Os número são iguais.')
