name = str(input('Digite seu nome completo: ')).strip()
separa = name.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(separa[0]))
print('Seu último nome é {}'.format(separa[-1]))