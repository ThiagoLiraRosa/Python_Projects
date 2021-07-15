sal=float(input('Digite o valor do Salário: '))
if sal >= 1250:
    aum10= (sal * 10 / 100) + sal
    print('Seu salário de {:.2f} teve aumento de 10%, e agora é de R$ {:.2f} '.format(sal, aum10))
else:
    aum15= (sal * 15 / 100) + sal
    print('Seu salário de {:.2f} teve aumento de 15%, e agora é de R$ {:.2f} '.format(sal, aum15))
