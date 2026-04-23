salario = float(input('Qual é o salário do Funcionário? R$'))

aumento = 15
novo_salario = salario * (1 + aumento / 100)
print('Um funcionário que ganhava R${}, com {}% de aumento, passa a receber R${:.2f}.'.format(salario, aumento, novo_salario))