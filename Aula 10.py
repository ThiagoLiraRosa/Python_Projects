'''tempo=int(input('Quantos anos tem seu Carro? '))
if tempo <=3:
    print('Seu carro é Novo!')
else:
    print('Seu carro é Velho!')
    print('---FIM---')'''

'''nome=str(input('Digite seu Nome: ')).upper()
if nome=='Thiago'.upper():
    print('Que nome Lindo !')
print('bom dia, {}.'.format(nome))'''

n1=float(input('Digite a primeira Nota: '))
n2=float(input('Digite a segunda Nota: '))
m=(n1+n2)/2
print('A Média deste Aluno é {:.2f}'.format(m))
if m>=6:
    print('Aluno Aprovado!')
else:
    print('Aluno Reprovado!')
