'''import random
n1=str(input('Digite o Primeiro Nome: '))
n2=str(input('Digite o Segundo Nome: '))
n3=str(input('Digite o Terceiro Nome: '))
n4=str(input('Digite o Quarto Nome: '))
lista= [n1, n2, n3, n4]
escolhido= random.choice(lista)
print('O aluno escolhido foi : {}'.format(escolhido) )'''

# Ou desta maneira:

from random import choice
n1=str(input('Digite o primeiro Nome: '))
n2=str(input('Digite o segundo Nome: ' ))
n3=str(input('Digite o terceiro Nome: '))
n4=str(input('Digite o quarto Nome: ' ))
lista=[n1, n2, n3, n4]
escolhido= choice(lista)
print('O aluno escolhido foi : {}'.format(escolhido) )

