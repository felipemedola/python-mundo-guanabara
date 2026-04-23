from math import radians, sin, cos, tan
angle = float(input('Digite o ângulo que você deseja: '))

sen = sin(radians(angle))
print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(angle, sen))
cos = cos(radians(angle))
print('O ângulo de {:.1f} tem o COSSENO de {:.2f}'.format(angle, cos))
tan = tan(radians(angle))
print('O ãngulo de {:.1f} tem a TANGENTE de {:.2f}'.format(angle, tan))




