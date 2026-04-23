s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    if s1 == s2 == s3 == s1:
        tipo_triangulo = 'EQUILÁTERO'
    elif s1 != s2 != s3 != s1:
        tipo_triangulo = 'ESCALENO'
    else:
        tipo_triangulo = 'ISÓSCELES'
    print(f'Os segmentos acima PODEM FORMAR um triângulo {tipo_triangulo}!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')
