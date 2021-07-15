a = float(input('Digite o tamanho da primeira linha: '))
b = float(input('Digite o tamanho da segunda linha: '))
c = float(input('Digite o tamanho da terceira linha: '))

if a < b + c and b < a + c and c < a + b:
    print('É possível ter um triangulo.')
else:
    print('Não é possível ter um triangulo')
