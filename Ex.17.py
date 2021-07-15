'''from math import hypot
co=float(input('Tamanho do Cateto Oposto: '))
ca=float(input('Tamanho do Cateto Adjacente: '))
hi=(co**2 + ca**2)**(1/2)
print('A hipotenusa va medir: {:.2f}'.format(hi))

OU

import math
co=float(input('Tamanho do Cateto Oposto: '))
ca=float(input('Tamanho do Cateto Adjacente: '))
hi= math.hypot(co, ca)
print('A hipotenusa va medir: {:.2f}'.format(hi))'''


from math import hypot
co=float(input('Tamanho do Cateto Oposto: '))
ca=float(input('Tamanho do Cateto Adjacente: '))
hi= hypot(co, ca)
print('A hipotenusa va medir: {:.2f}'.format(hi))
