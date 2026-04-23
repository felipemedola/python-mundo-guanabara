sen = str(input('Digite uma frase: ')).lower().strip()

print('A letra A aparece {} vezes na frase.'.format(sen.count('a')))
print('A primeira letra A apareceu na posição {}'.format(sen.find('a')))
print('A última letra A apareceu na posição {}'.format(sen.rfind('a')))