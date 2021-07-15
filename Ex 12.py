valor=float(input('Digite o valor do Produto: '))
novo= valor - (valor * 5 / 100)

print('O valor do produto com desconto é de R$ {:.2f} reais, '.format(novo))