'''import math
angulo =float(input('Digite um Angulo : '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem o Seno de {:.2f}, o Coseno de {:.2f}, e a Tangente de {:.2f}'.format(angulo, seno, coseno, tangente))'''

# Ou chamando diretamente um método

from math import sin, cos, tan, radians
angulo =float(input('Digite um Angulo : '))
seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O angulo de {} tem o Seno de {:.2f}, o Coseno de {:.2f}, e a Tangente de {:.2f}'.format(angulo, seno, coseno, tangente))

