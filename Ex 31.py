km=float(input('Digite a distancia em km: '))
if km <= 200:
    preço= km * 0.50
    print('O valor de sua passagem será de R$ {:.2f}'.format(preço))
else:
    preço= km * 0.45
    print('Ovalor de sua passagem será de R$ {:.2f}'.format(preço))
