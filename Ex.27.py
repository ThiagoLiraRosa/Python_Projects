n=str(input('Digite um nome completo: ')).strip()
nome=n.split()
print('O primeiro nome é: {}' .format(nome[0]))
print('O último nome é: {}'.format(nome[len(nome)-1]))
