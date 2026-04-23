numero = int(input('Digite um número inteiro: '))
opcao = int(input('Escolhas uma das bases para conversão: '
       '\n[ 1 ] converter para BINÁRIO'
       '\n[ 2 ] converter para OCTAL'
       '\n[ 3 ] converter para HEXADECIMAL'
       '\nSua opção: '))

if opcao == 1:
    novo_numero = bin(numero)
    print(f'{numero} convertido para BINÁRIO é igual a {novo_numero[2:]}')
elif opcao == 2:
    novo_numero = oct(numero)
    print(f'{numero} convertido para OCTAL é igual a {novo_numero[2:]}')
elif opcao == 3:
    novo_numero = hex(numero)
    print(f'{numero} convertido para HEXADECIMAL é igual a {novo_numero[2:]}')
else:
    print('Opção inválida. Tente novamente.')