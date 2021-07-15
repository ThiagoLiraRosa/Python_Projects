km=int(input('Qual a velocidade do Carro ? '))
if km<=80:
    print('Ok')
else:
    multa= (km - 80) * 7
    print('LIMITE DE VELOCIDADE EXCEDIDO!')
    print('Você foi multado em {} reais!'.format(multa))