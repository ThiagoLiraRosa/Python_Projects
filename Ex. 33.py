a = int(input('Digite o primeiro Número: '))
b = int(input('Digite o segundo Número: '))
c = int(input('Digite o terceiro Número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O Menor número é {}.'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O Maior número é {}.'.format(maior))
