from datetime import date

ano=int(input('Digite o ano para saber se é Bissexto. Digite 0 para saber se o ano atual é Bissexto ! '))

if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} É ano bissexto !'.format(ano))
else:
    print('{} Não é ano bissexto'.format(ano))