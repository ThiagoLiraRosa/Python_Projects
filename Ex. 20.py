'''import random
n1=str(input('Digite o 1º Nome: '))
n2=str(input('Digite o 2º Nome: '))
n3=str(input('Digite o 3º Nome: '))
n4=str(input('Digite o 4º Nome: '))

lista=[n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de Apresentação será: {}'.format(lista))'''

# Ou desta maneira:

from random import shuffle
n1=str(input('Digite o 1º Nome: '))
n2=str(input('Digite o 2º Nome: '))
n3=str(input('Digite o 3º Nome: '))
n4=str(input('Digite o 4º Nome: '))

lista=[n1, n2, n3, n4]
shuffle(lista)
print('A ordem de Apresentação será: {}'.format(lista))

