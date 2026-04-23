import math
cato = float(input('Comprimento do cateto oposto: '))
cata = float(input('Comprimento do cateto adjacente: '))
hip = math.hypot(cato, cata)
print('A hipotenusa vai medir {:.2f}'.format(hip))

'''hipotenusa = math.pow(cato, 2) + math.pow(cata, 2)
print('A hipotenusa vai medir {:.2f}'.format(math.sqrt(hipotenusa)))'''